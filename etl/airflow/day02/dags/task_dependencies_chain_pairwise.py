from datetime import datetime
from airflow.decorators import dag
from airflow.models.baseoperator import chain
from airflow.operators.dummy import DummyOperator


@dag(start_date=datetime(2021, 1, 1), catchup=False, tags=["task_dependencies"])
def task_dependencies_chain_pairwise():
    op1 = DummyOperator(task_id="op1")
    op2 = DummyOperator(task_id="op2")
    op3 = DummyOperator(task_id="op3")
    op4 = DummyOperator(task_id="op4")
    op5 = DummyOperator(task_id="op5")
    op6 = DummyOperator(task_id="op6")
    chain(op1, [op2, op3], [op4, op5], op6)


dag = task_dependencies_chain_pairwise()
