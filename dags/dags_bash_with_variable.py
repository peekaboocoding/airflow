from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator
from airflow.models import Variable
# 전역 공유변수 Variable
 ## xcom 은 특정 DAG 에서만 
 ## 모든 DAG 이 공유 
with DAG(
    dag_id="dags_bash_with_variable",
    schedule="10 9 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    # 1안) Variable 라이브러리 이용
    var_value = Variable.get("sample_key")
    bash_var_1 = BashOperator(
        task_id="bash_var_1",
        bash_command=f"echo variable:{var_value}"
    )
    # 2안) Jinja Template 이용 
    bash_var_2 = BashOperator(
        task_id="bash_var_2",
        bash_command=f"echo variable:{{var.value.sample_key}}"
    )