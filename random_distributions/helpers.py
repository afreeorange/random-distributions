from logging import NullHandler

import click

import random_distributions
from random_distributions.dist_base import BaseRealization

from .logger import log
from .plot import plot


def handle_generation(
    distribution: BaseRealization,
    number: int,
    output_file: str,
    graph: bool,
) -> None:
    log.info(
        f"Generating {number:,} realizations of the {distribution.name} distribution"
    )

    _output_file = output_file.rsplit(".", 1)[0] + ".txt"
    _output_graph = output_file.rsplit(".", 1)[0] + ".png"

    log.info(f"Writing output to {_output_file}")
    with open(_output_file, mode="w", encoding="utf-8") as f:
        for _ in range(number):
            f.write(f"{str(distribution.realization())}\n")

    if graph:
        log.info(f"Writing graph to {_output_graph}")
        plot(_output_file, _output_graph, number, distribution.name)


def common_cli_options(f):
    f = click.version_option(
        version=random_distributions.__version__,
    )(f)

    f = click.option(
        "--number",
        "-n",
        default=10000,
        help="Number of realizations to generate. Default is 10,000.",
    )(f)

    f = click.option(
        "--output-file",
        "-o",
        required=True,
        help="Output results to this file. Extension will be .txt",
    )(f)

    f = click.option(
        "--graph",
        "-g",
        is_flag=True,
        help=(
            "Draw a graph of the realizations in PNG. Name will "
            "be determined from the output filename."
        ),
    )(f)

    return f
