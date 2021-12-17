# Airflow DAGs

## Setup

```sh
docker compose up airflow-init
docker compose up -d
```

Open browser on http://localhost:8080 and login with `airflow` / `airflow`.

![dags](.imgs/dags.png)

## Declaring DAGs

For details read the documentation [here](https://airflow.apache.org/docs/apache-airflow/stable/concepts/dags.html)

We have three different ways to declare DAGs:

* `declare_dag_with_constructor`
* `declare_dag_with_context_manager`
* `declare_dag_with_decorator`

I prefer the decorator and will use that for further examples.

To dry run the DAG declarations simply do:

```sh
python {DAG_FILE}.py
```

It should exit without any errors if DAG is declared correctly.

## Task Dependencies

There are different ways to define the dependencies between the DAG tasks:

* `task_dependencies_operators`
* `task_depenendcies_downstream`
* `task_dependencies_chain`
* `task_dependencies_chain_pairwise`

## Postgres Connection

To connect to a postgres database, first create on the UI the connection:

* Conn ID: `postgres_default` (The default connection id used by the postgres operator)
* Conn Type: `postgres`
* Host: `postgres` (The connection info can be found on the `docker-compose.yaml` under `AIRFLOW__CORE__SQL_ALCHEMY_CONN` we re-use the running postgres for the example)
* Schema: `airflow`
* Login: `airflow`
* Password: `airflow`

DAGs:

* `operators_postgres` ([Reference](https://github.com/apache/airflow/tree/main/airflow/providers/postgres/example_dags))
* `pipeline_example` ([Reference](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html#pipeline-example))

## Pipeline Example

For details read the documentation [here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html#pipeline-example)

