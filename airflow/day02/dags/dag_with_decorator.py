from datetime import datetime
from airflow.decorators import dag
from airflow.operators.dummy import DummyOperator


@dag(start_date=datetime(2021, 1, 1), catchup=False, tags=["dags"])
def dag_with_decorator():
    op = DummyOperator(task_id="task")


dag = dag_with_decorator()
