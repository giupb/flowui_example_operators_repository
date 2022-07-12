from flowui.base_operator import BaseOperator
from flowui.client.s3_client import S3Client
from .model import OperatorModel

import random
import botocore


class LoadPhotoFromS3Operator(BaseOperator):
    
    def operator_function(self, operator_model: OperatorModel):
        s3_client = S3Client(bucket_name=operator_model.bucket_name)

        # Copy photo from S3 to mounted volume
        try:
            all_objs = s3_client.list_objects_from_bucket()
            random_obj = all_objs[random.randint(0, len(all_objs) - 1)]
            self.bucket.download_file(
                Key=random_obj.key, 
                Filename=self.results_path / random_obj.key
            )
            err = s3_client.download_s3_folder(
                s3_folder="/", 
                local_dir=self.results_path
            )
        except botocore.exceptions.ClientError as e:
            raise e

        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "results_message": "Photo successfully loaded to results path!",
            "results": dict(
                file_path=str(self.results_path / random_obj.key)
            )
        }
        return xcom_obj