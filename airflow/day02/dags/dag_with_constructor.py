from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator


dag = DAG(
    "dag_with_constructor",
    start_date=datetime(2021, 1, 1),
    tags=["dags"],
)
op = DummyOperator(task_id="task", dag=dag)
