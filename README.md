# Realizations of Some Common Statistical Distributions using Unif(0,1) PRNGs

## Abstract

This is a small library of some common discrete and continuous distributions realized using Unif(0,1) PRNGs generated using Python's `random.uniform` function which has a cycle-length of 2<sup>19,937</sup> - 1. It is implemented as a simple CLI that will generate a text file and graph of the requested distribution if needed. A complete set of example data and graphs may be found in the `examples` folder.

## Usage

You will need Python v3.9 and [Poetry](https://python-poetry.org/) installed globally to use this tool. The entry-point is a command called `realize`. 

### Overview

```console
# Install required dependencies
poetry install

# See all available distributions
poetry run realize --help

# See the input parameters for a particular distribution
poetry run realise triangular --help
```

* The default number of realizations is set to 100,000. You can change this by supplying a `--number` parameter to any command. 
* Graphs are not drawn by default. You can generate a graph by supplying a `--graph` flag. The output is always a PNG file. Its name is derived from whatever you specifed as the `--output-file`.
* Output files will be overwritten if they exist!

### Distributions

#### Bernoulli

Generate **Bern(p)** output with:

```console
poetry run realize bernoulli --probability 0.32 --output-file output.txt --graph
```

#### Binomial

Generate **Bin(n,p)** with:

```console
poetry run realize binomial --probability 0.34 --trials 1000 --output-file output.txt --graph
```

#### Geometric

Generate **Geom(p)** with:

```console
poetry run realize geometric --probability 0.32 --output-file output.txt --graph
```

#### Exponential

Generate **Exp(&lambda;)** with:

```console
poetry run realize exponential --lambda 2.5 --output-file output.txt --graph
```

#### Erlang

Generate **Erlang<sub>n</sub>(&lambda;)** with:

```console
poetry run realize erlang --lambda 3 --count 4 --output-file output.txt --graph
```

#### Standard Normal

Generate **Z(0,1)** with:

```console
poetry run realize standard_normal --output-file output.txt --graph
```

This method uses Box-Muller, so you will get a tuple/pair of values Z<sub>1</sub> and Z<sub>2</sub>

#### Gamma

Generate **Gamma(&alpha;, &beta;)** as **Gamma(shape, rate)** with:

```console
poetry run realize gamma --shape 17.5 --rate 6.25 --output-file output.txt --graph

poetry run realize gamma --shape 1 --rate 0.5 --output-file output.txt --graph
```

#### Laplace

Generate **Laplace(&mu;, b)** as **Laplace(location, scale)** with:

```console
poetry run realize laplace --location 0 --scale 1 --output-file output.txt --graph
```

#### Poisson

Generate **Pois(&lambda;)** between arrival times `[a,b]` with:

```console
poetry run realize poisson -a 2 -b 18 --lambda 0.6 --output-file output.txt --graph
```

#### Triangular

Generate **Tri(a, b, c)** as **Tri(lower, upper, mode)** with:

```console
poetry run realize triangular -a 1 -b 3 -c 2 --output-file output.txt --graph
```

#### Weibull

Generate **Weibull(&lambda;, k)** as **Weibull(scale, shape)** with:

```console
poetry run realize weibull --lambda 1 --shape 1.5 --output-file output.txt --graph
```

## Development

### Dependencies

The project uses 

* [Click](https://click.palletsprojects.com/en/7.x/) for the CLI
* [Seaborn](https://seaborn.pydata.org/) (with Matplotlib and Pandas) for its graphs

### Adding Distributions

Simple! Any new distribution must:

1. Provide the methods and properties specified in the `BaseRealization` abstract class in `dist_base.py`.
2. Implement a `cli` method using Click that accepts user input appropriately and then invokes the `helpers.handle_generation` method with the supplied parameters
3. Import, alias, and add the `cli` method in Step 2 to the entry-point's list of commands.

You would implement the actual realization in the `self.realization` of your distribution's class. You would make sure the user's not doing anything funky in `self.check` by yelling at them by raising a simple `ValueError` with a message of why their input was funky.

### `examples` Generation

```console
poetry run realize bernoulli --probability 0.32 --output-file examples/bernoulli.txt --graph
poetry run realize triangular -a 1 -b 3 -c 2 --output-file examples/triangular.txt --graph
poetry run realize exponential --lambda 2.5 --output-file examples/exponential.txt --graph
poetry run realize erlang --lambda 3 --count 4 --output-file examples/erlang.txt --graph
poetry run realize weibull --lambda 1 --shape 1.5 --output-file examples/weibull.txt --graph
poetry run realize standard_normal --output-file examples/standard_normal.txt --graph
poetry run realize geometric --probability 0.32 --output-file examples/geometric.txt --graph
poetry run realize bernoulli --probability 0.32 --output-file examples/bernoulli.txt --graph
poetry run realize binomial --probability 0.34 --trials 1000 --output-file examples/binomial.txt --graph
poetry run realize laplace --location 0 --scale 1 --output-file examples/laplace.txt --graph
poetry run realize gamma --shape 17.5 --rate 6.25 --output-file examples/gamma-1.txt --graph
poetry run realize gamma --shape 1 --rate 0.5 --output-file examples/gamma-2.txt --graph
poetry run realize poisson -a 2 -b 18 --lambda 0.6 --output-file examples/poisson.txt --graph
```

## License

MIT
