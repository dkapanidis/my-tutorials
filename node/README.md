# Node

Node can be installed using `brew`.

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
# list available versions from 17.*
nvm ls-remote 17
# install version v17.2.0
nvm install v17.2.0
# uninstall version 14
nvm uninstall 14
# use version (for current shell only)
nvm use 17
# set default version (for next shells)
nvm alias default v17.2.0
```
