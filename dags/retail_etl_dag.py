import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

# Get the absolute path to the project root
BASE_DIR = "/Users/vaish/databorn_etl_project/retail_etl/etl_pipeline_project"
data_file = os.path.join(BASE_DIR, 'data', 'raw', 'OnlineRetail.csv')
cleaned_file = os.path.join(BASE_DIR, 'data', 'processed', 'cleaned_data.csv')
output_file = os.path.join(BASE_DIR, 'output', 'final_report.csv')


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'retail_etl_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Retail ETL pipeline using PySpark and Airflow',
) as dag:
    
    start = EmptyOperator(task_id='start')

    check_raw_file = BashOperator(
        task_id='check_raw_file',
        bash_command=f'test -f "{data_file}" || (echo "Missing {data_file}. Please download and place it." && exit 1)',
    )

    clean_data = BashOperator(
        task_id='clean_data',
        bash_command=f'spark-submit {os.path.join(BASE_DIR, "spark_jobs", "clean_data.py")} --input "{data_file}" --output "{cleaned_file}"',
    )

    aggregate_data = BashOperator(
        task_id='aggregate_data',
        bash_command=f'spark-submit {os.path.join(BASE_DIR, "spark_jobs", "aggregate_data.py")} --input "{cleaned_file}" --output "{output_file}"',
    )

    finish = EmptyOperator(task_id='finish')

    start >> check_raw_file >> clean_data >> aggregate_data >> finish 