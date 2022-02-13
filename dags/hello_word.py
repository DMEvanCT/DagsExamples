from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
    print("Hello World")

with DAG(dag_id="hello_world_dag",
    start_date=datetime(2022, 1, 1),
    schedule_interval="@hourly",
    catchup=False) as dag:

    task1 = PythonOperator(
    task_id="hello_word",
    python_callable=hello_word)

task1