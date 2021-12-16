# Airflow Intro

For details read the documentation [here](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)

## Setup

Download the `docker-compose.yaml`:

```sh
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.2.2/docker-compose.yaml'
### change to the following value on docker-compose.yaml:
#    AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
```

Make sure you have enough memory configured to Docker engine (should be at least 4G):

```sh
$ docker run --rm "debian:buster-slim" bash -c 'numfmt --to iec $(echo $(($(getconf _PHYS_PAGES) * $(getconf PAGE_SIZE))))'
4.1G
```

Setting the right Airflow user

```sh
mkdir -p ./dags ./logs ./plugins
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

Initialize database:

```sh
$ docker compose up airflow-init
airflow-init_1       | [2021-12-15 11:33:14,778] {manager.py:214} INFO - Added user airflow
airflow-init_1       | User "airflow" created with role "Admin"
airflow-init_1       | 2.2.2
airflow_airflow-init_1 exited with code 0
```

Start airflow:

```sh
docker compose up -d
docker compose logs -f
# wait for the following lines
day01-airflow-webserver-1  | [2021-12-16 11:35:16 +0000] [49] [INFO] Listening at: http://0.0.0.0:8080 (49)
```

Open browser on http://localhost:8080 and login with `airflow` / `airflow`.

![dags](.imgs/dags.png)


Unpause the DAG `hello-world` by clicking the toggle button before the name of the DAG. This will trigger the DAG for the first time and we can see on the logs the returned message:

```
[2021-12-16, 11:48:25 UTC] {python.py:152} INFO - Done. Returned value was: Hello world from first Airflow DAG!
[2021-12-16, 11:48:25 UTC] {taskinstance.py:1280} INFO - Marking task as SUCCESS. dag_id=hello_world, task_id=hello_task, execution_date=20211214T120000, start_date=20211216T114824, end_date=20211216T114825
```
