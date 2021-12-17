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

