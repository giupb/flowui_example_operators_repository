from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Download Image from Picsum (https://picsum.photos/)
    """

    width_pixels: int = Field(
        default=200,
        description='Width in number of pixels',
        gt=10
    )
    height_pixels: int = Field(
        default=200,
        description='Height in number of pixels',
        gt=10
    )


class OutputModel(BaseModel):
    """
    Download Image from Picsum (https://picsum.photos/)
    """

    message: str = Field(
        default="",
        description="Output message to log"
    )
    output_file_path: str = Field(
        description='The path to the downloaded file'
    )