from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Example Operator
    """

    input_arg_1: str = Field(
        default='default',
        description='description'
    )


class OutputModel(BaseModel):
    """
    Example Operator
    """
    data: list = Field(
        description="Output list with airbnb data"
    )
    message: str = Field(description="Message to log")


class SecretsModel(BaseModel):
    """
    Example Operator Secrets
    """

    API_KEY: str = Field(
        description="API key"
    )