import math
from random import uniform

import click

from .dist_base import BaseRealization
from .helpers import common_cli_options, handle_generation


class Distribution(BaseRealization):
    def __init__(self, rate_param):
        self.rate_param = rate_param

    @property
    def type(self):
        return "Continuous"

    @property
    def name(self):
        return "Exponential"

    @property
    def params(self):
        return f"lambda={self.rate_param}"

    def realization(self):
        U = uniform(0, 1)
        X = (-1 / self.rate_param) * math.log(U)

        return X

    def check(self):
        if self.rate_param < 0:
            raise ValueError("Lambda/Rate Param must be greater than zero.")


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
def cli(rate_param, number, output_file, graph):
    d = Distribution(rate_param)
    handle_generation(d, number, output_file, graph)
