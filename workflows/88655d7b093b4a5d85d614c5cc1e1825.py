
from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from flowuipackage.tasks.task import Task

dag_config_0 = {'name': 'luizworkflow1', 'schedule_interval': None, 'start_date': None, 'catchup': False, 'workflow_id': '88655d7b093b4a5d85d614c5cc1e1825'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']

dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    task_1 = Task(dag, **{'freq_min': 0.2, 'freq_max': 0.3, 'include_results_in_report': True, 'dag_id': 'tttt', 'task_id': 'task_1', 'operator': 'AgreementOperator', 'deploy_mode': 'local'})()
    task_2 = Task(dag, **{'freq_min': 1, 'freq_max': 300, 'include_results_in_report': True, 'dag_id': 'tttt', 'task_id': 'task_2', 'operator': 'BandPassFilterOperator', 'deploy_mode': 'local'})()
    task_2.set_upstream([globals()[t] for t in ['task_1']])
