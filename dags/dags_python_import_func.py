from airflow import DAG 
import datetime # C:\Program Files\Python38\Lib\datetime.py
import pendulum
from airflow.operators.python import PythonOperator
'''
- 동일 경로부터 잡기 때문에 plugins.common.common_func 되어야 함.
    - 해당 내용을 위해 .env 파일에 PYTHONPATH 를 잡아줌
    - 경로 설정 내용은 반영해줄 필요 x ▶ .gitignore 에 반영
    
- Airflow의 설정정보에는 /opt/airflow/plugins 까지 경로가 잡혀 있기에 하위 디렉터리부터 명시되어야 함.
    - 예를 들어 코드상에서 from plugins.common.common_func 명시를 하게 되면
      /opt/airflow/plugins/plugins 가 되기에 에러를 발생함. 
      ▶ local 에서 전체적인 경로를 잡아주고 
      ▶ Airflow 컨테이너에서는 plugins 하위부터 인식하기에 코드에 plugins 하위 지점부터 반영해주면 됨.
'''
from common.common_func import get_sftp

import random

with DAG(
    dag_id="dags_python_import_func",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2023, 12, 28, tz="Asia/Seoul"),
    catchup=False
) as dag: 
    task_get_sftp = PythonOperator(
        task_id='task_get_sftp',
        python_callable=get_sftp,
    )

    task_get_sftp