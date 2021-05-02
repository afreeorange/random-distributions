"""
Simple module that generates a histogram from a CSV file.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .logger import log


def plot(
    path_to_input_file,
    path_to_output_file,
    number_of_points,
    title,
):
    try:
        data = pd.read_csv(path_to_input_file)

        sns.histplot(
            data,
            legend=False,
            fill=False,
            kde=True,
        )

        plt.axis("off")
        plt.ylabel("")
        plt.xlabel("")
        plt.title(f"{number_of_points:,} realizations of the {title} Distribution")
        plt.savefig(path_to_output_file, dpi=350)

    except Exception as e:
        log.error(f"Error generating plot: {str(e)}")
