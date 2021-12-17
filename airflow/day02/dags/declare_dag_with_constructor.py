from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator


dag = DAG(
    "declare_dag_with_constructor",
    start_date=datetime(2021, 1, 1),
    tags=["declare_dag"]
)
op = DummyOperator(task_id="task", dag=dag)
