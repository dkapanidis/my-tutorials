# PHP Setup

This setup is to get started with Python development.

## pyenv

To handle multiple versions use `pyenv`.

To install `pyenv`:

```sh
brew install pyenv
```

Some useful commands:

```sh
# List managed versions
❯ pyenv versions
  system
* 3.7.9 (set by ~/.pyenv/version)
  3.8.9
  3.11.5
# Configure global version
$ pyenv global 3.11.5
# Configure local version (per directory)
$ pyenv local 3.8.9
```