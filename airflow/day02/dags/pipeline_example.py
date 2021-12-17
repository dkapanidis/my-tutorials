from datetime import datetime
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
import requests

@dag(start_date=datetime(2021, 1, 1), catchup=False, tags=["task_dependencies"])
def pipeline_example():
    @task
    def get_data():
        url = "https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/pipeline_example.csv"

        response = requests.request("GET", url)

        with open("/opt/airflow/dags/files/employees.csv", "w") as file:
            for row in response.text.split("\n"):
                file.write(row + "\n")

        postgres_hook = PostgresHook(postgres_conn_id="LOCAL")
        conn = postgres_hook.get_conn()
        cur = conn.cursor()

    get_data()


dag = pipeline_example()
