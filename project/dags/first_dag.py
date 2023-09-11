print("starting")
try:
  from datetime import datetime, timedelta
  from airflow import DAG
  from airflow.operators.python import PythonOperator
  from datetime import datetime
  # import pandas as pd

  print("All Dag modules are ok ........")
except Exception as e:
  print("Error {}".format(e))

def _first_function_execute():
  print("Hello world ")
  return "Hello world"

with DAG(
  dag_id="first_dag",
  schedule_interval ="@daily",
  default_args={
    "owner": "admin",
    "retries": 1,
    "retry": timedelta(minutes=5),
    "start_date": datetime(2023, 8, 29),
  },
  catchup=False) as dag:

  first_function_execute = PythonOperator(
    task_id="first_function_execute",
    python_callable=_first_function_execute
  )

  # first_function_execute

  print ("completed")
