from datetime import datetime
from airflow import DAG
from airflow.operators.dummy import DummyOperator


with DAG(
    "declare_dag_with_context_manager",
    start_date=datetime(2021, 1, 1),
    tags=["declare_dag"],
) as dag:
    op = DummyOperator(task_id="task")
