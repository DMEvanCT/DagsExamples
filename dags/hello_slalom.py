from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def helloWorld():
    print("Hello Evan")

def welcomeToSlalomDemo():
    print("Welcome to the Slalom Airflow Demo")

with DAG(dag_id="hello_slalom_demo",
    start_date=datetime(2022, 1, 1),
    schedule_interval="@hourly",
    catchup=False) as dag:

    task1 = PythonOperator(
    task_id="hello_word",
    python_callable=helloWorld)

    task2 = PythonOperator(
    task_id="hello_slalom",
    python_callable=welcomeToSlalomDemo)

[task1, task2]