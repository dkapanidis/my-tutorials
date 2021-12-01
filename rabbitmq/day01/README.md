# Day 1 - Basics

RabbitMQ is a message broker.

## Start RabbitMQ

To start a RabbitMQ using docker compose:

```sh
docker compose up rabbitmq -d
```

open http://localhost:15672 and login with `guest` / `guest` credentials.

## RabbitMQ CLI

RabbitMQ comes with `rabbitmqctl` tool:

```sh
docker compose exec rabbitmq rabbitmqctl
```

## RabbitMQ Producer

Let's create our first producer. This will send JSON messages in a `domain-events` durable queue.

To start a producer:

```sh
docker compose up producer
```

> NOTE: Make sure the RabbitMQ is running before starting the producer.

