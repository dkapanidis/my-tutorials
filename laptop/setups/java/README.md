# Java Setup

This setup is to get started with Java development.

## jenv

To handle multiple versions use `jenv`:

To install `jenv`:

```sh
brew install jenv
```

Some useful commands:

```sh
# List managed JDKs
$ jenv versions
  system
  oracle64-1.6.0.39
* oracle64-1.7.0.11 (set by /Users/hikage/.jenv/version)
# Configure global version
$ jenv global oracle64-1.6.0.39
# Configure local version (per directory)
$ jenv local oracle64-1.6.0.39
# Configure shell instance version
$ jenv shell oracle64-1.6.0.39
```