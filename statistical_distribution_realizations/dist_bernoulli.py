import math
from random import uniform

import click

from .dist_base import BaseRealization
from .helpers import common_cli_options, handle_generation


class Distribution(BaseRealization):
    def __init__(self, p):
        self.p = p

    @property
    def type(self):
        return "Discrete"

    @property
    def params(self):
        return f"p={self.p}"

    @property
    def name(self):
        return "Bernoulli"

    def realization(self):
        U = uniform(0, 1)
        X = 0

        if U <= self.p:
            X = 1

        return X

    def check(self):
        if self.p > 1:
            raise ValueError("Probability cannot be greater than 1")

        if self.p <= 0:
            raise ValueError("Probability cannot be lower than 0")


@click.command()
@common_cli_options
@click.option(
    "--probability",
    "-p",
    help="Probability of event",
    required=True,
    type=float,
)
def cli(probability, number, output_file, graph):
    d = Distribution(probability)
    handle_generation(d, number, output_file, graph)
