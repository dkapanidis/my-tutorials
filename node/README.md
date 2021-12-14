# Node

Node can be installed using `brew`.

## node version

I use the same node version on all projects: `v16.13.1`.

## nvm

To handle multiple versions use `nvm`.

To install `nvm`:

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
```

Some useful commands:

```sh
# list installed versions
nvm list
# list available versions from 16.*
nvm ls-remote 16
# install version v16.13.1
nvm install v16.13.1
# uninstall version 14
nvm uninstall 14
# use version (for current shell only)
nvm use 16
# set default version (for next shells)
nvm alias default v16.13.1
```
