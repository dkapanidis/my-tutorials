# Airflow DAGs

For details read the documentation [here](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)

## Setup

```sh
docker compose up airflow-init
docker compose up -d
```

Open browser on http://localhost:8080 and login with `airflow` / `airflow`.

![dags](.imgs/dags.png)

## DAGs

Now we have the following DAGs loaded:

* `tutorial` from [Airflow](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)


## Tutorial DAG

We can run partially specific tasks by doing the following:

```sh
# Run airflow CLI inside a container in interactive mode
$ ./airflow bash

## testing task print_date
$ airflow tasks test tutorial print_date 2015-06-01
...
[2021-12-16 12:42:26,047] {subprocess.py:74} INFO - Running command: ['bash', '-c', 'date']
[2021-12-16 12:42:26,061] {subprocess.py:85} INFO - Output:
[2021-12-16 12:42:26,066] {subprocess.py:89} INFO - Thu Dec 16 12:42:26 UTC 2021

## testing task sleep
$ airflow tasks test tutorial sleep 2015-06-01
...
[2021-12-16 12:43:16,570] {subprocess.py:74} INFO - Running command: ['bash', '-c', 'sleep 5']

## testing task templated
$ airflow tasks test tutorial templated 2015-06-01
...
[2021-12-16 12:43:55,843] {subprocess.py:74} INFO - Running command: ['bash', '-c', '\n\n    echo "2015-06-01"\n    echo "2015-06-08"\n    echo "Parameter I passed in"\n\n    echo "2015-06-01"\n    echo "2015-06-08"\n    echo "Parameter I passed in"\n\n    echo "2015-06-01"\n    echo "2015-06-08"\n    echo "Parameter I passed in"\n\n    echo "2015-06-01"\n    echo "2015-06-08"\n    echo "Parameter I passed in"\n\n    echo "2015-06-01"\n    echo "2015-06-08"\n    echo "Parameter I passed in"\n']
```

We can also run the entire DAG to test it:

```sh
## testing dag tutorial
$ airflow dags test tutorial 2021-12-15
...
[2021-12-16 12:47:21,528] {dagrun.py:602} INFO - DagRun Finished: dag_id=tutorial, execution_date=2021-12-15T00:00:00+00:00, run_id=backfill__2021-12-15T00:00:00+00:00, run_start_date=2021-12-16 12:47:06.189703+00:00, run_end_date=2021-12-16 12:47:21.527935+00:00, run_duration=15.338232, state=success, external_trigger=False, run_type=backfill, data_interval_start=2021-12-15T00:00:00+00:00, data_interval_end=2021-12-16T00:00:00+00:00, dag_hash=None
```

Or we can do a `backfill` to run the DAG multiple times for a specific date range and also register the state in the DB:

```sh
## bacfill dag tutorial
$ airflow dags backfill tutorial --start-date 2015-06-01 --end-date 2015-06-14
...
[2021-12-16 12:52:36,000] {backfill_job.py:397} INFO - [backfill progress] | finished run 14 of 14 | tasks waiting: 0 | succeeded: 42 | running: 0 | failed: 0 | skipped: 0 | deadlocked: 0 | not ready: 0
```
