from airflow import DAG 
import datetime # C:\Program Files\Python38\Lib\datetime.py
import pendulum
from airflow.operators.python import PythonOperator

import random


with DAG(
    dag_id="dags_python_operator",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 12, 28, tz="Asia/Seoul"),
    catchup=False
) as dag: 
    def select_fruit():
        fruit = ['사과','딸기','포도','귤']
        rand_int = random.randint(0,3)
        print(fruit[rand_int])
    
    py_t1 = PythonOperator(
        task_id='py_t1',
        python_callable=select_fruit,
    )
    py_t1 