from flowui.base_operator import BaseOperator
from flowui.client.s3_client import S3Client
from .models import InputModel, OutputModel

import random
import botocore


class LoadPhotoFromS3Operator(BaseOperator):
    
    def operator_function(self, input_model: InputModel):
        s3_client = S3Client(bucket_name=input_model.bucket_name)

        # Copy photo from S3 to mounted volume
        try:
            all_objs = s3_client.list_objects_from_bucket()
            random_obj = all_objs[random.randint(0, len(all_objs) - 1)]
            output_file_path = str(self.results_path / random_obj.key)
            self.bucket.download_file(
                Key=random_obj.key, 
                Filename=output_file_path
            )
        except botocore.exceptions.ClientError as e:
            raise e

        return OutputModel(
            message="Photo successfully downloaded!",
            output_file_path=output_file_path
        )