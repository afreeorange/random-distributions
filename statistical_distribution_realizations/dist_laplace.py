import math
from random import uniform

import click

from .dist_base import BaseRealization
from .helpers import common_cli_options, handle_generation
from .logger import log


class Distribution(BaseRealization):
    def __init__(self, location, scale):
        self.location = location
        self.scale = scale

    @property
    def type(self):
        return "Continuous"

    @property
    def params(self):
        return f"mu={self.location}, b={self.scale}"

    @property
    def name(self):
        return "Laplace"

    def realization(self):
        U = uniform(0.0, 1.0)

        sign = 0
        if (U - 0.5) > 0:
            sign = 1
        else:
            sign = -1

        X = self.location - self.scale * sign * math.log(1 - 2 * abs(U - 0.5))

        return X

    def check(self):
        if self.scale < 0:
            raise ValueError("Scale parameter cannot be lower than zero")


@click.command()
@common_cli_options
@click.option(
    "--location",
    "-m",
    help="Mu, the location parameter",
    required=True,
    type=float,
)
@click.option(
    "--scale",
    "-b",
    help="The scale parameter",
    required=True,
    type=float,
)
def cli(location, scale, number, output_file, graph):
    d = Distribution(location, scale)
    handle_generation(d, number, output_file, graph)
