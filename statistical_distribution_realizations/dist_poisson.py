import math
from random import uniform

import click

from .dist_base import BaseRealization
from .helpers import common_cli_options, handle_generation


class Distribution(BaseRealization):
    def __init__(self, a, b, rate, number):
        self.a = a
        self.b = b
        self.rate = rate
        self.number = number

    @property
    def type(self):
        return "Discrete"

    @property
    def params(self):
        return f"a={self.a}, b={self.b}, rate={self.rate}"

    @property
    def name(self):
        return "Poisson"

    # Unlike all other distributions, this is not a point-realization but an
    # array of sorted and shifted U(0,1)
    def realization(self):
        return sorted(
            [self.a + (self.b - self.a) * uniform(0, 1) for _ in range(self.number)]
        )

    def check(self):
        if self.a < 0 or self.b < 0 or self.rate < 0:
            raise ValueError("All Poisson parameters must be greater than zero.")


@click.command()
@common_cli_options
@click.option(
    "--a",
    "-a",
    help="a",
    required=True,
    type=int,
)
@click.option(
    "--b",
    "-b",
    help="b",
    required=True,
    type=int,
)
@click.option(
    "--lambda",
    "-l",
    "rate",
    help="Lambda, the arrival rate",
    required=True,
    type=float,
)
def cli(a, b, rate, number, output_file, graph):
    d = Distribution(a, b, rate, number)
    handle_generation(d, number, output_file, graph)
