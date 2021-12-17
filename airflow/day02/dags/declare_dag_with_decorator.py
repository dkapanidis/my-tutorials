from datetime import datetime
from airflow.decorators import dag, task
from airflow.models.baseoperator import BaseOperator
from airflow.operators.email import EmailOperator
from airflow.operators.dummy import DummyOperator


@dag(
    start_date=datetime(2021, 1, 1),
    catchup=False,
)
def declare_dag_with_decorator():
    op = DummyOperator(task_id="task")


dag = declare_dag_with_decorator()
