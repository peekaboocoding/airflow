from airflow import DAG
import pendulum
from airflow.operators.bash import BashOperator

with DAG (
    dag_id = "dags_bash_with_macro_eg1",
    schedule="10 0 L * *",
    start_date=pendulum.datetime(2024, 1, 3, tz="Asia/Seoul"),
    catchup=False
) as dag:
    bask_task_1 = BashOperator(
        task_id='bask_task_1',
        # START_DATE: 전월 말일, END_DATE: 1일 전
        # .in_timezone 한국 표준시간대 적용
        # .relativedelta 
        # ds : yyyy-mm-dd
        # dt : yyyy-mm-ddTHH:MI:SS
        env={'START_DATE':'{{data_interval_start.in_timezone("Asia/Seoul") | ds}}', 
             'END_DATE':'{{ (data_interval_end.in_timezone("Asia/Seoul") - macro.dateutil.relativedelta.relativedelta(days=1)) | ds}}'
        }, 
        bash_command='echo "START_DATE: $START_DATE" && echo "END_DATE: $END_DATE"'
    )