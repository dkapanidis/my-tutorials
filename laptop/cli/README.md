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

Some generic CLI tools:

* [HTTPie](https://httpie.io/): A simple yet powerful command-line HTTP and API testing client for the API era.
* [jq](https://stedolan.github.io/jq/): a lightweight and flexible command-line JSON processor.
* [yq](https://mikefarah.gitbook.io/yq/): a lightweight and portable command-line YAML processor.
* [htop](https://github.com/htop-dev/htop): htop is an interactive system-monitor process-viewer and process-manager.
* [hey](https://github.com/rakyll/hey): HTTP load generator.
* [websocat](https://github.com/vi/websocat): Command-line client for WebSockets, like netcat (or curl) for ws:// with advanced socat-like functions.

Some k8s related CLI tools:

* [hadolint](https://github.com/hadolint/hadolint): Dockerfile linter, validate inline bash, written in Haskell.
* [helm](https://helm.sh/): The package manager for Kubernetes.
* [octant](https://octant.dev/): Visualize your Kubernetes workloads.
* [minikube](https://minikube.sigs.k8s.io/docs/start/): minikube is local Kubernetes.
* [rbac-lookup](https://github.com/FairwindsOps/rbac-lookup): RBAC Lookup is a CLI that allows you to easily find Kubernetes roles and cluster roles bound to any user, service account, or group name.
* [kubetail](https://github.com/johanhaleby/kubetail): Bash script to tail Kubernetes logs from multiple pods at the same time.
* [kubeseal](https://github.com/bitnami-labs/sealed-secrets): A Kubernetes controller and tool for one-way encrypted Secrets.
* [k3d](https://k3d.io/): k3d is a lightweight wrapper to run k3s.
* [pack](https://buildpacks.io/): CLI for building apps using Cloud Native Buildpacks.

Some archived CLI tools:

* [glow](https://github.com/charmbracelet/glow):Render markdown on the CLI, with pizzazz.
* [pow](http://pow.cx/): Pow is a zero-config Rack server for Mac OS X.
* [figlet](http://www.figlet.org/): FIGlet is a program for making large letters out of ordinary text.
