# Laptop > CLI

Setup of CLI environment and useful tools.

## Setup CLI

### iTerm

For Terminal emulator I use [iTerm](https://iterm2.com/). Installed with `brew`.

### Zsh

My favorite shell is [zsh](https://www.zsh.org/). Installed with `brew`.

To set zsh as your default shell, execute the following:

```sh
sudo sh -c "echo $(which zsh) >> /etc/shells" && chsh -s $(which zsh)
```

## Useful CLI Tools

* [HTTPie](https://httpie.io/): A simple yet powerful command-line HTTP and API testing client for the API era.
* [htop](https://github.com/htop-dev/htop): htop is an interactive system-monitor process-viewer and process-manager.
* [jq](https://stedolan.github.io/jq/): a lightweight and flexible command-line JSON processor.
* [yq](https://mikefarah.gitbook.io/yq/): a lightweight and portable command-line YAML processor.
* [websocat](https://github.com/vi/websocat): Command-line client for WebSockets, like netcat (or curl) for ws:// with advanced socat-like functions.

