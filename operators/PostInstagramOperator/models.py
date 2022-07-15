from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Post image on Instagram
    """

    input_image_path: str = Field(
        description='Path to the image to be posted'
    )


class OutputModel(BaseModel):
    """
    Post image on Instagram
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )