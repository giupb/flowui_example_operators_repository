from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Get photo from S3 path
    """

    bucket_name: str = Field(
        default='bucket-name',
        description='this is the name of the bucket'
    )


class OutputModel(BaseModel):
    """
    Get photo from S3 path
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )
    output_file_path: str = Field(
        description='Path to the downloaded file'
    )