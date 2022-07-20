
from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from flowui.tasks.task import Task


dag_config_0 = {'schedule_interval': '@once', 'start_date': '2022-01-10', 'catchup': False, 'dag_id': 'example_workflow_1'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']

dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    task_1 = Task(dag, **{'dag_id': 'example_workflow_1', 'task_id': 'task_1', 'operator': 'ExampleOperator', 'deploy_mode': 'local-bash'})()

