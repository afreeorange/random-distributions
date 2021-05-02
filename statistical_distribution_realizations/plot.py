"""
Simple module that generates a histogram from a CSV file.
"""

from math import dist
from statistical_distribution_realizations.dist_base import BaseRealization
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .logger import log


def plot(
    path_to_input_file: str,
    path_to_output_file: str,
    number_of_points: int,
    distribution: BaseRealization,
) -> None:
    try:
        data = pd.read_csv(path_to_input_file)

        sns.histplot(
            data,
            legend=False,
            fill=False,
            kde=True if distribution.type == "Discrete" else False,
        )

        params = f"({distribution.params})" if distribution.params else ""

        plt.title(f"{distribution.name} {params} N={number_of_points:,}")
        plt.savefig(path_to_output_file, dpi=350)

    except Exception as e:
        log.error(f"Error generating plot: {str(e)}")
