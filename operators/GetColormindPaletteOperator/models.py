from pydantic import BaseModel, Field
from enum import Enum


class PaletteModelType(str, Enum):
    default = "default"
    ui = "ui"
    makoto_shinaki = "makoto_shinkai"
    metroid_fusion = "metroid_fusion"
    akira_film = "akira_film"
    flower_photography = "flower_photography"


class InputModel(BaseModel):
    """
    Get color palette from image, using Colormind (http://colormind.io)
    """
    input_file_path: str = Field(
        default=None,
        description="Path to the input file."
    )
    input_image_data: str  = Field(
        default=None,
        description="Input image data."
    )
    model: PaletteModelType = Field(
        default="default",
        description="Model to generate color palette."
    )
    save_as_file: bool = Field(
        default=False,
        description='Save result as file. If false, return palette data in XCOM'
    )


class OutputModel(BaseModel):
    """
    Get color palette from image, using Colormind (http://colormind.io)
    """
    message: str = Field(
        default="",
        description="Output message to log."
    )
    output_palette_file_path: str = Field(
        default=None,
        description='Path to the generated palette file.'
    )
    output_palette_data: str = Field(
        default=None,
        description='Generated palette data.'
    )