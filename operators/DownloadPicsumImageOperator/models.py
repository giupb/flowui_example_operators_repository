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
    save_as_file: bool = Field(
        default=False,
        description='Save result as file. If false, return image data in XCOM'
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
        default=None,
        description='The path to the downloaded file'
    )
    image_data: str = Field(
        default=None,
        description="Downloaded image data"
    )