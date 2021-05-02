import click

from .dist_triangular import cli as triangular


@click.group()
def entry_point():
    """
    Generates realizations of a few discrete and continuous distributions.
    Type one of the commands listed below to see additional flags
    """
    pass


entry_point.add_command(triangular, "triangular")
