import math
from random import uniform

import click

from .dist_base import BaseRealization
from .helpers import common_cli_options, handle_generation
from .logger import log


class Distribution(BaseRealization):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

        log.info(f"Triangular distribution with a={a}, b={b}, c={c}")

    @property
    def _cdf(self):
        return (self.c - self.a) / (self.b - self.a)

    @property
    def params(self):
        return f"(a={self.a}, b={self.b}, c={self.c})"

    @property
    def name(self):
        return "Triangular"

    def realization(self):
        U = uniform(0, 1)
        X = 0

        if U < self._cdf:
            X = self.a + math.sqrt(U * (self.b - self.a) * (self.c - self.a))
        else:
            X = self.b - math.sqrt((1 - U) * (self.b - self.a) * (self.b - self.c))

        return X

    def check(self):
        if not (self.a < self.b and self.a <= self.c and self.c <= self.b):
            raise ValueError("Invalid params. Rules: a < c and a ≤ c ≤ b")


@click.command()
@common_cli_options
@click.option(
    "--a",
    "-a",
    help="Lower limit of distribution",
    required=True,
    type=int,
)
@click.option(
    "--b",
    "-b",
    help="Upper limit of distribution",
    required=True,
    type=int,
)
@click.option(
    "--c",
    "-c",
    help="Mode of distribution",
    required=True,
    type=int,
)
def cli(a, b, c, number, output_file, graph):
    d = Distribution(a, b, c)
    handle_generation(d, number, output_file, graph)
