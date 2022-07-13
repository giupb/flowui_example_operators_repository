from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Download random file from Github
    """

    repository_name: str = Field(
        description='The name of the target repository'
    )
    branch: str = Field(
        default="main",
        description='The branch to be used'
    )
    folder_path: str = Field(
        description='The folder path within the repository'
    )