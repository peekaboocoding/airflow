from airflow import DAG 
import datetime # C:\Program Files\Python38\Lib\datetime.py
import pendulum
from airflow.decorators import task

'''
 - 수행날짜 24.01.01
'''
with DAG(
    dag_id="dags_python_show_templates",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2023, 12, 31, tz="Asia/Seoul"),
    catchup=True
) as dag: 
    @task(task_id="python_task")
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()