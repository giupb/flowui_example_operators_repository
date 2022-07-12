from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Gets photo from S3 path
    """

    bucket_name: str = Field(
        default='atlas-photos',
        description='this is the name of the bucket'
    )