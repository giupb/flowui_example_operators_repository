from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel

import requests
from pathlib import Path
from io import BytesIO
from PIL import Image


class DownloadPicsumImageOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        # Request random image
        response = requests.get(f'https://picsum.photos/{input_model.width_pixels}/{input_model.height_pixels}')
        img = Image.open(BytesIO(response.content))

        image_path = str(Path(self.results_path) / "image.jpeg")
        img.save(fp=image_path)
        self.logger.info("Image downloaded")

        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "message": f"Image successfully downloaded to: {image_path}",
            "other_custom_info": dict(
                image_path=str(image_path)
            )
        }
        return OutputModel(
            message="Image successfully downloaded!",
            output_file_path=image_path
        )

