from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def print_hello():
    return "Hello world from Airflow DAG"


dag = DAG(
    "hello_world",
    description="Hello World DAG",
    schedule_interval="0 * * * *",
    start_date=datetime(2021, 1, 1),
    catchup=False,
)

hello_operator = PythonOperator(
    task_id="hello_task", python_callable=print_hello, dag=dag
)

hello_operator
