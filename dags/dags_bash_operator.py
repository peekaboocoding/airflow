from airflow import DAG 
import datetime
import pendulum
from airflow.operators.bash import BashOperator

'''
  # start_date : 
    - tz : utc 기준 9시간 더 늦게 돌게됨. 
    - catchup : False - 누락된 부분에 대해 돌지 않음. 
              : True - 누락된 부분에 대해 한꺼번에 돌게 됨.
    - dagrun_timeout : 해당 시간 이후에 timeout 발생 
    - tags : Airflow UI 상에 있는 파란색 박스 
    - params : DAG 밑에 task 들을 두는데 , 공통적으로 필요한 parameter에 대해 입력하게 한다. 
'''
with DAG(
    dag_id="dags_bash_operator", 
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2023, 12, 26, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    # tags=["example", "example2"],
    # params={"example_key": "example_value"}
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )
    bash_t2 = BashOperator( # 객체명 
        task_id="bash_t2",  # task id (node 개념) .. * 객체명과 task 명이 동일해야 찾기 쉬움
        bash_command="echo $HOSTNAME",
    )
    # task 들의 수행순서, 관계 .. 명시
    bash_t1 >> bash_t2