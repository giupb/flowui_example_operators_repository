from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Upload photo from mounted volume to S3 folder
    """

    s3_bucket_name: str = Field(
        default='bucket-name',
        description='this is the name of the bucket'
    )
    s3_folder_name: str = Field(
        default='edited',
        description='this is the folder path within the bucket'
    )