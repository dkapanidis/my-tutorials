from datetime import datetime
from airflow.decorators import dag
from airflow.models.baseoperator import cross_downstream
from airflow.operators.dummy import DummyOperator


@dag(start_date=datetime(2021, 1, 1), catchup=False, tags=["task_dependencies"])
def task_dependencies_cross_downstream():
    op1 = DummyOperator(task_id="op1")
    op2 = DummyOperator(task_id="op2")
    op3 = DummyOperator(task_id="op3")
    op4 = DummyOperator(task_id="op4")
    cross_downstream([op1, op2], [op3, op4])


dag = task_dependencies_cross_downstream()
