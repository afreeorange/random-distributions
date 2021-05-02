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
    def name(self):
        return "Triangular"

    def realization(self):
        return uniform(0.0, 1.0) + uniform(0.0, 1.0)

    def check(self):
        return True


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
