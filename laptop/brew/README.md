# Laptop > Brew

Brew is a convenient package manager for MacOS.

### Setup

To install brew:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Brew Install

Run `brew install <APP>` to install an app.

e.g.

```sh
brew install git
```

### Brew Doctor

Run `brew doctor` every so often to make sure everything is ok with brew installations.

### Brew Cleanup

Run `brew cleanup` every so often to remove old versions.

### Brew Update

Run `brew update` every so often to update all package definitions (formulae) and Homebrew itself.

### Brew Upgrade

Run `brew upgrade` every so often to upgrade the installed apps.

### My favorite tools

* [Homebrew] for package management
* [Homebrew Services] addon to manage services
* [Git] for version control
  * [Git Flow] to manage branch worflow
* [Zsh] a beautiful terminal
* [VirtualBox] to run VMs
* [Docker] to run containers
* [Minikube] to run Kubernetes
* [AWS CLI] to manage AWS
* [Eksctl] to manage AWS EKS Clusters
* [Google Cloud SDK] to manage Google Cloud
* [Kubernetic] to manage Kubernetes
* [Kubectx] to switch faster between clusters and namespaces
* [Kube-ps1] to add Kubernetes prompt info on Shell
* [Kubetail] to tail Kubernetes logs
* [Kops] to manage Kubernetes Production Clusters
* [Helm] to manage Kubernetes Charts
* [Z] to track into your most used directories
* [HTTPie] a command line HTTP client with an intuitive UI

It should take less than 15 minutes to install (depends on your machine).

[Homebrew]: https://brew.sh/
[Homebrew Services]: https://github.com/Homebrew/homebrew-services
[Git]: https://git-scm.com/
[Git Flow]: https://github.com/nvie/gitflow
[Zsh]: https://ohmyz.sh/
[VirtualBox]: https://www.virtualbox.org/wiki/Downloads
[Docker]: http://docker.com/
[Minikube]: https://kubernetes.io/docs/setup/minikube/
[AWS CLI]: https://aws.amazon.com/cli/
[Eksctl]: https://github.com/weaveworks/eksctl
[Google Cloud SDK]: https://cloud.google.com/sdk/install
[Kubernetic]: https://www.kubernetic.com
[Kubectx]: https://github.com/ahmetb/kubectx
[Kube-ps1]: https://github.com/jonmosco/kube-ps1
[Kubetail]: https://github.com/johanhaleby/kubetail
[Kops]: https://github.com/kubernetes/kops
[Helm]: https://github.com/helm/helm
[Z]: https://github.com/rupa/z
[httpie]: https://httpie.org/
