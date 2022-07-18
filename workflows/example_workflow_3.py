
from datetime import datetime
from dateutil.parser import parse
from airflow import DAG
from flowui.tasks.task import Task
from flowui.schemas.from_upstream import FromUpstream


dag_config_0 = {'schedule_interval': '@once', 'start_date': '2022-01-10', 'catchup': False, 'dag_id': 'example_workflow_3'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']

dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}

with DAG(**dag_config) as dag:
    task_1 = Task(dag, **{'repository_name': 'Tauffer-Consulting/atlas_project', 'branch': 'main', 'folder_path': 'original', 'dag_id': 'example_workflow_3', 'task_id': 'task_1', 'operator': 'DownloadFileFromGithubOperator', 'deploy_mode': 'local-bash'})()
    task_2 = Task(dag, **{'effect': 'pencil', 'input_file_path': FromUpstream(upstream_task_id='task_1', output_arg='output_file_path'), 'dag_id': 'example_workflow_3', 'task_id': 'task_2', 'operator': 'ApplyCV2FilterOperator', 'deploy_mode': 'local-bash'})()
    task_3 = Task(dag, **{'repository_name': 'Tauffer-Consulting/atlas_project', 'branch': 'main', 'input_file_path': FromUpstream(upstream_task_id='task_2', output_arg='output_file_path'), 'dag_id': 'example_workflow_3', 'task_id': 'task_3', 'operator': 'UploadFileToGithubOperator', 'deploy_mode': 'local-bash'})()
    task_2.set_upstream([globals()[t] for t in ['task_1']])
    task_3.set_upstream([globals()[t] for t in ['task_2']])
