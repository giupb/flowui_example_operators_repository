from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Gets photo from S3 path
    """

    bucket_name: str = Field(
        default='bucket-name',
        description='this is the name of the bucket'
    )