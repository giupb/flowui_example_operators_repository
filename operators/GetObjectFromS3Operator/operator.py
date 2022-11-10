from flowui.base_operator import BaseOperator
import boto3
from .models import InputModel, OutputModel
from botocore.exceptions import ClientError


class GetObjectFromS3Operator(BaseOperator):
    def operator_function(self, input_model: InputModel):
        """
        Get object from S3 and return it as a bytestring
        """
        s3_client = boto3.client("s3")
    
        bucket = input_model.bucket_name
        path = input_model.path
        try:
            resp = s3_client.get_object(Bucket=bucket, Key=path)
        except ClientError as e:
            self.logger.error(e)
            raise e

        return OutputModel(
            bytes_object=resp.get("Body").read()
        )