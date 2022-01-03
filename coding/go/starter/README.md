# Go - Starter - REST API

This is a demo of building a REST API with [Golang] & [SwaggerUI].

It contains an API to manage the library of a **Movie streaming service**.

## Setup

Install the following dependencies before starting to develop:

```sh
go get github.com/ahmetb/govvv
go get github.com/pilu/fresh
go get github.com/swaggo/swag/cmd/swag
```

## Dependencies

These are the important pieces we use:

* [go mod] for dependency management
* [govvv] for version info


[go mod]: https://blog.golang.org/using-go-modules
[govvv]: https://github.com/ahmetb/govvv

[Golang]: https://golang.org/
[SwaggerUI]: https://swagger.io/tools/swagger-ui/

### Start

To start do

```sh
make deps
make run
```

Open on browser http://localhost:8080 to get a view of the Swagger UI and interact with the APIs.
