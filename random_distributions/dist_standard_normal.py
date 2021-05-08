import math
from random import uniform

import click

from .dist_base import BaseRealization
from .helpers import common_cli_options, handle_generation


class Distribution(BaseRealization):
    @property
    def type(self):
        return "Continuous"

    @property
    def name(self):
        return "Standard Normal"

    @property
    def params(self):
        return f""

    def realization(self):
        U1 = uniform(0, 1)
        U2 = uniform(0, 1)

        Z1 = math.sqrt(-2 * math.log(U1)) * math.cos(2 * math.pi * U2)
        Z2 = math.sqrt(-2 * math.log(U1)) * math.sin(2 * math.pi * U2)

        return Z1, Z2

    def check(self):
        pass


@click.command()
@common_cli_options
def cli(number, output_file, graph) -> None:
    d = Distribution()
    handle_generation(d, number, output_file, graph)
