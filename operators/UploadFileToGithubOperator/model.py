from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Upload file to Github
    """

    repository_name: str = Field(
        description='The name of the target repository'
    )
    branch: str = Field(
        default="main",
        description='The branch to be used'
    )
    file_path: str = Field(
        description='The file path within the repository'
    )