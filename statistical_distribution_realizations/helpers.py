import sys
from logging import NullHandler

import click
import progressbar

import statistical_distribution_realizations
from statistical_distribution_realizations.dist_base import BaseRealization

from .logger import log
from .plot import plot


def handle_generation(
    distribution: BaseRealization,
    number: int,
    output_file: str,
    graph: bool,
) -> None:
    log.info(f"Generating {number:,} realizations")

    try:
        distribution.check()
    except Exception as e:
        log.error(f"Oh no: {str(e)}")
        sys.exit(1)

    bar = progressbar.ProgressBar(
        widgets=[
            progressbar.Bar(),
            progressbar.Counter(),
        ],
        max_value=number,
    ).start()
    o = output_file.rsplit(".", 1)[0]
    _output_file = f"{o}.txt"
    _output_graph = f"{o}.png"

    log.info(f"Writing output to {_output_file}")
    with open(_output_file, mode="w", encoding="utf-8") as f:
        for _ in range(number):
            f.write(f"{str(distribution.realization())}\n")
            bar.update(_ + 1)

    bar.finish()

    if graph:
        log.info(f"Writing graph to {_output_graph}")
        plot(_output_file, _output_graph, number, distribution)


def common_cli_options(f):
    f = click.version_option(
        version=statistical_distribution_realizations.__version__,
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
