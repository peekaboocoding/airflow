from airflow import DAG
import pendulum
import datetime
from airflow.operators.bash import BashOperator


with DAG(
    dag_id="dags_bash_select_fruit",
    schedule="10 0 * * 6#1",
    start_date=pendulum.datetime(2023, 12, 27, tz="Asia/Seoul"),
    catchup=False
) as dag:
    t1_orange = BashOperator(
        task_id="t1_orange",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE"

    )
    t2_apple = BashOperator(
        task_id="t2_apple",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh APPLE"
    )
    t3_ANY = BashOperator(
        task_id="t3_ANY",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ANY"
    )

    t1_orange >> t2_apple >> t3_ANY