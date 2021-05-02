import math
from random import uniform

import click

from .dist_base import BaseRealization
from .helpers import common_cli_options, handle_generation
from .logger import log


class Distribution(BaseRealization):
    def __init__(self, rate_param, n):
        self.rate_param = rate_param
        self.n = n

    @property
    def type(self):
        return "Continuous"

    @property
    def name(self):
        return "Erlang"

    @property
    def params(self):
        return f"lambda={self.rate_param}, n={self.n}"

    def realization(self):
        U = uniform(0, 1)

        Us = uniform(0, 1)
        for _ in range(self.n - 1):
            Us = Us * uniform(0, 1)

        X = (-1 / self.rate_param) * math.log(Us)

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
@click.option(
    "--count",
    "-n",
    "count",
    help="Number of individual exponential distributions",
    required=True,
    type=int,
)
def cli(rate_param, count, number, output_file, graph):
    d = Distribution(rate_param, count)
    handle_generation(d, number, output_file, graph)
