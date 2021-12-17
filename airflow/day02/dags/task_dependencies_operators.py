from datetime import datetime
from airflow.decorators import dag
from airflow.operators.dummy import DummyOperator


@dag(start_date=datetime(2021, 1, 1), catchup=False, tags=["task_dependencies"])
def task_dependencies_operators():
    """
    DAG to send server IP to email.

    :param email: Email to send IP to. Defaults to example@example.com.
    :type email: str
    """

    op1 = DummyOperator(task_id="op1")
    op2 = DummyOperator(task_id="op2")
    op3 = DummyOperator(task_id="op3")
    op4 = DummyOperator(task_id="op4")
    op1 >> [op2, op3]
    op3 << op4


dag = task_dependencies_operators()
