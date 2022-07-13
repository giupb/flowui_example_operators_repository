from flowui.base_operator import BaseOperator
from flowui.client.github_rest_client import GithubRestClient
from .model import OperatorModel

from pathlib import Path
import PIL.Image as Image
import base64


class LoadFileFromGithubOperator(BaseOperator):
    
    def operator_function(self, operator_model: OperatorModel):
        github_client = GithubRestClient()

        # Load image produced from previous task
        upstream_task_id = list(self.upstream_tasks.keys())[0]
        previous_task_results_path = Path(self.upstream_tasks[upstream_task_id]["results"]["file_path"])
        file_target = f"edited/{previous_task_results_path.name}"

        with open(file_target, "rb") as image_file:
            encoded_string = image_file.read()

        # TODO - NET WORKING YET, IMAGES ARE NOT BEING PROPERLY UPLOADED AS IMAGE TYPES
        github_client.create_file(
            repo_name=operator_model.repository_name, 
            file_path=file_target, 
            content=encoded_string
        )
        file_url = f"https://github.com/{operator_model.repository_name}/raw/{operator_model.branch}/{file_target}"
        

        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "results_message": "File successfully uploaded to Github!",
            "results": dict(
                file_url=file_url
            )
        }
        return xcom_obj