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
        description="Path to the input file."
    )
    model: PaletteModelType = Field(
        default="default",
        description="Model to generate color palette"
    )


class OutputModel(BaseModel):
    """
    Get color palette from image, using Colormind (http://colormind.io)
    """
    message: str = Field(
        default="",
        description="Output message to log"
    )
    output_palette_path: str = Field(
        description='Path to the generated palette file'
    )