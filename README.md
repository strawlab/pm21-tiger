# pm21-tiger

## Introduction

This is the course material for PM-21, Winter Semester 2022-2023 (year of the
Tiger), Faculty of Biology, University of Freiburg. The instructors are Prof.
Dr. Andrew Straw and Nils Wenke.

## Run interactively at https://strawlab-rp2.zoologie.uni-freiburg.de

We strongly recommend that you install Anaconda Python on your own computer -
this gives you the tools to run your own code after the class is over on your
own PC. We will help you install Anaconda python and the packages we use in the
course. While we are doing that, for the first few days (or for the entire
course), you may use our server. This will be taken offline shortly after the
course is done.

You may use our jupyter hub at https://strawlab-rp2.zoologie.uni-freiburg.de .
To login, use your lastname, lower-case as username (e.g. 'müller'). Your
password will be discussed in class.

## Installation with Anaconda

Download the Anaconda Distribution from
[here](https://www.anaconda.com/products/distribution).

We will demonstrate how to setup an Anaconda environment in class. Use our
[`environment.yml`](https://raw.githubusercontent.com/strawlab/pm21-tiger/main/environment.yml)
file to setup your `pm21-tiger` environment in Anaconda. **Failure to use the
`environment.yml` file for the class may result in incompatibility with the
exercises in the course.**

## Links

## The Python Tutor - extremely highly recommended

http://pythontutor.com/

## Some useful Python data science cheat sheets

- https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
- http://www.utc.fr/~jlaforet/Suppl/python-cheatsheets.pdf

## Run on your computer with anaconda

```
conda env create -f environment.yml
conda activate pm21-tiger
# Alternatively, try "source activate pm21-tiger"
jupyter notebook
```

## Troubleshooting

### Note for macOS users

Before starting `jupyter notebook` from the command line, you may like to type:

    ulimit -n 4096

This will solve [OSError: [Errno 24] Too many open files](https://github.com/jupyterlab/jupyterlab/issues/6727).

## Code of conduct

Anyone who interacts with this software in any space, including but not limited
to this GitHub repository, must follow our [code of
conduct](code_of_conduct.md).
