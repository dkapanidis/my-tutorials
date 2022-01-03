# Python Tutorial

This is a collection of high-speed learning tutorial for Python.

It's high-speed because it's not focused on learning the internals of python language but on practical use-cases from low-level to more abstract ones.

Each day depends on previous lessons learned, but if you know the scope of a specific day you can skip ahead.


- [Day 1 - Basic Intro](day01/README.md)
- [Day 2 - Parquet Format](day02/README.md)
- [Day 3 - Spark SQL, DataFrames and Datasets](day03/README.md)
- [Day 4 - S3](day04/README.md)

## pyenv

To handle multiple Python versions use `pyenv`.

To install `pyenv` use [pyenv-installer](https://github.com/pyenv/pyenv-installer):

```sh
curl https://pyenv.run | bash
```

Some useful commands:

```sh
# list installed versions
pyenv versions
# list available versions
pyenv install --list
# install version 3.8.9
pyenv install 3.8.9
# uninstall version 3.7.9
pyenv uninstall 3.7.9
# set local Python version
pyenv local 3.8.9
# set global Python version
pyenv global 3.8.9
# verify pyenv installation and development tools to build pythons.
pyenv doctor
```
