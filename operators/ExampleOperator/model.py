from pydantic import BaseModel, Field


class OperatorModel(BaseModel):
    """
    Example Operator
    """

    arg1: str = Field(
        default='default',
        description='description'
    )