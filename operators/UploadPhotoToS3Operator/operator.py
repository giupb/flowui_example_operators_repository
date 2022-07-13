from flowui.base_operator import BaseOperator
from flowui.client.s3_client import S3Client
from .model import OperatorModel

from pathlib import Path
import botocore


class UploadPhotoToS3Operator(BaseOperator):
    
    def operator_function(self, operator_model: OperatorModel):
        s3_client = S3Client(bucket_name=operator_model.s3_bucket_name)

        try:
            # Load image downloaded with previous task
            upstream_task_id = list(self.upstream_tasks.keys())[0]
            previous_task_results_path = self.upstream_tasks[upstream_task_id]["results"]["file_path"]
            target_s3_path = f"{operator_model.s3_folder_name}/{Path(previous_task_results_path).name}"
            s3_client.upload_file_to_s3(
                object_key=target_s3_path, 
                file_path=previous_task_results_path
            )
        except botocore.exceptions.ClientError as e:
            raise e

        # Push results through XComs
        xcom_obj = {
            "results_message": "Photo successfully uploaded to S3!",
        }
        return xcom_obj