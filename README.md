# A Small Library of some Common Statistical Distributions

## Abstract

## Usage

### Overview

```console
# See all available distributions
poetry run realize --help

# See the input parameters for a particular distribution
poetry run realise triangular --help
```

### Complete Set of Examples

Some notes:

* The default number of realizations is set to 100,000. You can change this by supplying a `--number` parameter to any command.
* You can specify 

```console
# Triangular
poetry run realize triangular -a 1 -b 3 -c 2 --output-file test.txt --graph

# Exponential 
poetry run realize exponential --lambda 2.5 --output-file test.txt --graph

# Erlang
poetry run realize erlang --lambda 3 --count 4 --output-file test.txt --graph

# Weibull
poetry run realize weibull --lambda 1 --beta 1.5 --output-file test.txt --graph

# Standard Normal
poetry run realize standard_normal --output-file test.txt --graph

# Geometric
poetry run realize geometric --probability 0.32 --output-file test.txt --graph

# Bernoulli
poetry run realize bernoulli --probability 0.32 --output-file test.txt --graph

# Binomial
poetry run realize binomial --probability 0.34 --trials 1000 --output-file test.txt --graph

# Laplace
poetry run realize laplace --location 0 --scale 1 --output-file test.txt --graph
```

## Development

## TODO

* [ ] Gamma
* [ ] Poisson
* [x] Bernoulli
* [x] Binomial
* [x] Erlang
* [x] Exponential
* [x] Geometric
* [x] Laplace
* [x] Standard Normal
* [x] Triangular
* [x] Weibull

## License

MIT
