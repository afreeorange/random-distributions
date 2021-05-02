import math
from random import uniform

import click

from .dist_base import BaseRealization
from .helpers import common_cli_options, handle_generation


class Distribution(BaseRealization):
    def __init__(self, trials, p):
        self.trials = trials
        self.p = p

    @property
    def type(self):
        return "Discrete"

    @property
    def params(self):
        return f"n={self.trials}, p={self.p}"

    @property
    def name(self):
        return "Binomial"

    def realization(self):
        X = 0

        for _ in range(self.trials):
            U = uniform(0, 1)
            if U <= self.p:
                X += 1

        return X

    def check(self):
        if self.p > 1:
            raise ValueError("p cannot be greater than 1")

        if self.p <= 0:
            raise ValueError("Probability cannot be lower than 0")


@click.command()
@common_cli_options
@click.option(
    "--trials",
    "-n",
    help="Number of trials",
    required=True,
    type=int,
)
@click.option(
    "--probability",
    "-p",
    help="Probability of event",
    required=True,
    type=float,
)
def cli(trials, probability, number, output_file, graph):
    d = Distribution(trials, probability)
    handle_generation(d, number, output_file, graph)
