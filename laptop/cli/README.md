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

For Zsh Theme I use [powerlevel10k](https://github.com/romkatv/powerlevel10k):

```sh
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/powerlevel10k
echo 'source ~/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
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
* [kind](https://github.com/kubernetes-sigs/kind): Kubernetes IN Docker.
* [rbac-lookup](https://github.com/FairwindsOps/rbac-lookup): RBAC Lookup is a CLI that allows you to easily find Kubernetes roles and cluster roles bound to any user, service account, or group name.
* [kubetail](https://github.com/johanhaleby/kubetail): Bash script to tail Kubernetes logs from multiple pods at the same time.
* [stern](https://github.com/wercker/stern): ⎈ Multi pod and container log tailing for Kubernetes.
* [kubeseal](https://github.com/bitnami-labs/sealed-secrets): A Kubernetes controller and tool for one-way encrypted Secrets.
* [k3d](https://k3d.io/): k3d is a lightweight wrapper to run k3s.
* [pack](https://buildpacks.io/): CLI for building apps using Cloud Native Buildpacks.
* [krew](https://github.com/kubernetes-sigs/krew): 📦 Find and install kubectl plugins.
* [tektoncd-cli](https://github.com/tektoncd/cli): A CLI for interacting with Tekton.
* [argocd](https://argo-cd.readthedocs.io/en/stable/cli_installation/): GitOps continuous delivery tool for Kubernetes.
* [skaffold](https://skaffold.dev/): Local Kubernetes Development.
* [kubernetic](https://www.kubernetic.com/): The Kubernetes Desktop Client - Cluster management, simplified.

Recording & Live coding CLI tools:

* [keycastr](https://github.com/keycastr/keycastr): KeyCastr, an open-source keystroke visualizer.
* [doitlive](https://doitlive.readthedocs.io/en/stable/): Because sometimes you need to do it live.
* [ngrok](https://ngrok.com/): Ngrok exposes local servers behind NATs and firewalls to the public internet over secure tunnels.
* [tmate](https://tmate.io/): Instant terminal sharing.

Some archived CLI tools:

* [glow](https://github.com/charmbracelet/glow): Render markdown on the CLI, with pizzazz.
* [upterm](https://github.com/railsware/upterm): an IDE in the world of terminals.
* [pow](http://pow.cx/): Pow is a zero-config Rack server for Mac OS X.
* [figlet](http://www.figlet.org/): FIGlet is a program for making large letters out of ordinary text.
* [cowsay](https://en.wikipedia.org/wiki/Cowsay): generates ASCII art pictures of a cow with a message.
* [vagrant](https://www.vagrantup.com/): Development Environments Made Easy.
* [hugo](https://gohugo.io/): open-source static site generator.

Some networking tools:

* [socat](https://www.redhat.com/sysadmin/getting-started-socat): The socat utility is a relay for bidirectional data transfers between two independent data channels.

Some DB tools:

* [sqlite](https://www.sqlite.org/index.html): small, fast, self-contained, high-reliability, full-featured, SQL database engine.

Some Java tools:

* [springboot](https://spring.io/projects/spring-boot): Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications that you can "just run".

Some Go tools:

* [upx](https://upx.github.io/): the Ultimate Packer for eXecutables.

3rd party tools:

* [stripe](https://stripe.com/docs/stripe-cli): developer tool to help you build, test, and manage your integration with Stripe directly from your terminal.

Presentation tools:

* [slidev](https://sli.dev/) Presentation Slides for Developers.
