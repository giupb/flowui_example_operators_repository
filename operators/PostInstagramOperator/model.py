from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Post image on Instagram
    """

    arg1: str = Field(
        default='default',
        description='description'
    )