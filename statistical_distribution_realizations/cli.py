import click

from .dist_bernoulli import cli as bernoulli
from .dist_binomial import cli as binomial
from .dist_erlang import cli as erlang
from .dist_exponential import cli as exponential
from .dist_geometric import cli as geometric
from .dist_laplace import cli as laplace
from .dist_standard_normal import cli as standard_normal
from .dist_triangular import cli as triangular
from .dist_weibull import cli as weibull


@click.group()
def entry_point():
    """
    Generates realizations of a few discrete and continuous distributions.
    Type one of the commands listed below to see additional flags
    """
    pass


entry_point.add_command(bernoulli, "bernoulli")
entry_point.add_command(binomial, "binomial")
entry_point.add_command(erlang, "erlang")
entry_point.add_command(exponential, "exponential")
entry_point.add_command(geometric, "geometric")
entry_point.add_command(laplace, "laplace")
entry_point.add_command(standard_normal, "standard_normal")
entry_point.add_command(triangular, "triangular")
entry_point.add_command(weibull, "weibull")
