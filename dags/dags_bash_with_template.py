from airflow import DAG 
import datetime
import pendulum
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_with_template", 
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 12, 26, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command='echo "data_interval_end: {{data_interval_end}}"',
    )
    bash_t2 = BashOperator( # 객체명 
        task_id="bash_t2",  # task id (node 개념) .. * 객체명과 task 명이 동일해야 찾기 쉬움
        env={
        'START_DATE' : '{{data_interval_start | ds}}',
        'END_DATE' : '{{data_interval_end}}',
        },
        bash_command='echo $START_DATE && echo $END_DATE'
    )
    
    bash_t1 >> bash_t2  