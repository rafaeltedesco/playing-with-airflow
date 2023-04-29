from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'tedesco',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 29),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'mydag',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval='0 0 * * *',
)

def task1():
    print("Task 1")

def task2():
    print("Task 2")

op1 = PythonOperator(
    task_id='task_1',
    python_callable=task1,
    dag=dag,
)

op2 = PythonOperator(
    task_id='task_2',
    python_callable=task2,
    dag=dag,
)

op1 >> op2
