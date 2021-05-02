import math
from random import uniform

import click

from .dist_base import BaseRealization
from .helpers import common_cli_options, handle_generation
from .logger import log


class Distribution(BaseRealization):
    def __init__(self, rate_param, beta):
        self.rate_param = rate_param
        self.beta = beta

    @property
    def type(self):
        return "Continuous"

    @property
    def name(self):
        return "Weibull"

    @property
    def params(self):
        return f"lambda={self.rate_param}, beta={self.beta}"

    def realization(self):
        U = uniform(0, 1)
        X = (1 / self.rate_param) * ((-1 * math.log(U)) ** (1 / self.beta))

        return X

    def check(self):
        if self.rate_param < 0:
            raise ValueError("Lambda/Rate Param must be greater than zero.")

        if self.beta < 0:
            raise ValueError("Shape param must be greater than zero.")


@click.command()
@common_cli_options
@click.option(
    "--lambda",
    "-l",
    "rate_param",
    help="Lambda; the rate parameter",
    required=True,
    type=float,
)
@click.option(
    "--beta",
    "-b",
    help="Beta; the shape parameter",
    required=True,
    type=float,
)
def cli(rate_param, beta, number, output_file, graph):
    d = Distribution(rate_param, beta)
    handle_generation(d, number, output_file, graph)
