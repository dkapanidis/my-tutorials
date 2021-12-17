from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.postgres.operators.postgres import PostgresOperator
import requests
import csv


@dag(
    schedule_interval="0 0 * * *",
    start_date=datetime.today() - timedelta(days=2),
    dagrun_timeout=timedelta(minutes=60),
    catchup=False,
    tags=["postgres"],
)
def pipeline_example():
    create_employees_table = PostgresOperator(
        task_id="create_employees_table",
        sql="""
            CREATE TABLE IF NOT EXISTS Employees (
                 "Serial Number" numeric not null constraint employees_pk primary key,
                 "Company Name" text,
                 "Employee Markme" text,
                 "Description" text,
                 "Leave" integer
             );
          """,
    )

    create_employees_temp_table = PostgresOperator(
        task_id="create_employees_temp_table",
        sql="""
            CREATE TABLE IF NOT EXISTS "Employees_temp" (
                 "Serial Number" numeric not null constraint employees_temp_pk primary key,
                 "Company Name" text,
                 "Employee Markme" text,
                 "Description" text,
                 "Leave" integer
             );

          """,
    )

    @task
    def get_data():
        url = "https://raw.githubusercontent.com/apache/airflow/main/docs/apache-airflow/pipeline_example.csv"

        response = requests.request("GET", url)

        with open("/opt/airflow/dags/files/employees.csv", "w") as file:
            file.write(response.text)

        postgres_hook = PostgresHook()
        conn = postgres_hook.get_conn()
        cur = conn.cursor()
        with open("/opt/airflow/dags/files/employees.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row.
            for row in reader:
                print(row)
                cur.execute(
                    'INSERT INTO "Employees_temp" VALUES (%s, %s, %s, %s, %s)', row
                )

    @task
    def merge_data():
        query = """
                delete
                from "Employees" e using "Employees_temp" et
                where e."Serial Number" = et."Serial Number";

                insert into "Employees"
                select *
                from "Employees_temp";
                """
        try:
            postgres_hook = PostgresHook()
            conn = postgres_hook.get_conn()
            cur = conn.cursor()
            cur.execute(query)
            conn.commit()
            return 0
        except Exception as e:
            return 1

    (
        [create_employees_table, create_employees_temp_table]
        >> get_data()
        >> merge_data()
    )


dag = pipeline_example()
