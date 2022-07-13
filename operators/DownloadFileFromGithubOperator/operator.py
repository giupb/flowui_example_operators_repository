from flowui.base_operator import BaseOperator
from flowui.client.github_rest_client import GithubRestClient
from .model import OperatorModel

import PIL.Image as Image
import random
import io


class DownoadFileFromGithubOperator(BaseOperator):
    
    def operator_function(self, operator_model: OperatorModel):
        github_client = GithubRestClient()

        # Copy photo from Github repository to mounted volume
        all_files = github_client.list_contents(
            repo_name=operator_model.repository_name,
            folder_path=operator_model.file_path,
        )
        random_obj = all_files[random.randint(0, len(all_files) - 1)]

        image = Image.open(io.BytesIO(random_obj.decoded_content))
        output_file_path = str(self.report_path / random_obj.name)
        image.save(output_file_path)

        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "results_message": "Photo successfully downloaded to results path!",
            "results": dict(
                file_path=output_file_path
            )
        }
        return xcom_obj