import sys
from typing import Callable

import click
import progressbar

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
    log.info(f"{distribution.name} Distribution: {distribution.params}")
    log.info(f"Generating {number:,} realizations")

    try:
        distribution.check()
    except Exception as e:
        log.error(f"Oh no: {str(e)}")
        sys.exit(1)

    o = output_file.rsplit(".", 1)[0]
    _output_file = f"{o}.txt"
    _output_graph = f"{o}.png"

    log.info(f"Writing output to {_output_file}")

    with open(_output_file, mode="w", encoding="utf-8") as f:
        # Poisson is slightly weird because it doesn't have any
        # point-realizations. You generate a set of Unif(0,1) and sort them
        # (and shift them if need be) for the interarrival times 🤷‍♂️ The
        # result in this case comes sorted. It's an array and not a single
        # number.
        if distribution.name == "Poisson":
            log.warn("Poisson distribution! Sorting might take some time for large n!")

            # There is no way to refine this type AFAIK
            __ = distribution.realization()
            if isinstance(__, list):
                for _ in __:
                    f.write(f"{_}\n")

        else:
            bar = progressbar.ProgressBar(
                widgets=[
                    progressbar.Bar(),
                    progressbar.Counter(),
                ],
                max_value=number,
            ).start()

            for _ in range(number):
                X = distribution.realization()

                # Standard Normal is the only one that returns a Tuple
                # (because we use Box-Muller)
                if isinstance(X, tuple):
                    f.write(f"{X[0]}, {X[1]}\n")
                else:
                    f.write(f"{X}\n")

                bar.update(_ + 1)

            bar.finish()

    if graph:
        log.info(f"Writing graph to {_output_graph}")
        plot(_output_file, _output_graph, number, distribution)


def common_cli_options(f: Callable) -> Callable:
    f = click.version_option(
        version=random_distributions.__version__,
    )(f)

    f = click.option(
        "--number",
        "-n",
        default=100000,
        help="Number of realizations to generate. Default is 100,000.",
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
