import math
from random import uniform

import click

from .dist_base import BaseRealization
from .helpers import common_cli_options, handle_generation


class Distribution(BaseRealization):
    def __init__(self, shape, rate):
        self.shape = shape
        self.rate = rate

    @property
    def type(self):
        return "Continuous"

    @property
    def name(self):
        return "Gamma"

    @property
    def params(self):
        return f"alpha={self.shape}, beta={self.rate}"

    def _gam1(self):
        b = (math.e + self.rate) / math.e
        Y = 0
        X = 0

        while True:
            U = uniform(0.0, 1.0)
            V = uniform(0.0, 1.0)
            W = b * U

            if W < 1:
                Y = W ** (1 / self.rate)

                if V < (math.e ** (-1 * Y)):
                    X = Y / self.shape
                    break
            else:
                Y = (-1) * math.log((b - W) / self.rate)
                if V <= (Y ** (self.rate - 1)):
                    X = Y / self.shape
                    break

        return X

    def _gam2(self):
        a = (2 * self.rate - 1) ** (-0.5)
        b = self.rate - math.log(4)
        c = self.rate + (1 / a)
        d = 1 + math.log(4.5)

        X = 0

        while True:
            U1 = uniform(0.0, 1.0)
            U2 = uniform(0.0, 1.0)

            V = a * math.log(U1 / (1 - U1))
            Y = self.rate * (math.e ** V)
            Z = (U1 ** 2) * U2
            W = b + c * V - Y

            if W + d - 4.5 * Z >= 0:
                X = Y / self.shape
                break

            else:
                if W >= math.log(Z):
                    X = Y / self.shape
                    break

        return X

    def realization(self):
        if self.rate < 1:
            return self._gam1()
        else:
            return self._gam2()

    def check(self):
        if self.shape < 0 or self.rate < 0:
            raise ValueError("Both shape and rate must be greater than zero")


@click.command()
@common_cli_options
@click.option(
    "--shape",
    "-s",
    help="Alpha, the shape parameter",
    required=True,
    type=float,
)
@click.option(
    "--rate",
    "-r",
    help="Beta, the rate parameter",
    required=True,
    type=float,
)
def cli(shape, rate, number, output_file, graph):
    d = Distribution(shape, rate)
    handle_generation(d, number, output_file, graph)
