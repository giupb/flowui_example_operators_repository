from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel

import requests
from pathlib import Path
from io import BytesIO
from PIL import Image
import base64


class DownloadPicsumImageOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        # Request random image
        response = requests.get(f'https://picsum.photos/{input_model.width_pixels}/{input_model.height_pixels}')

        if input_model.save_as_file:
            img = Image.open(BytesIO(response.content))
            image_path = str(Path(self.results_path) / "image.jpeg")
            img.save(fp=image_path)
            self.logger.info("Image downloaded")
            message = f"Image successfully downloaded and saved to: {image_path}"
            output_file_path = image_path
            image_data = None
        else:
            message = "Image successfully downloaded and sent through XCOM."
            output_file_path = None
            image_data = base64.b64encode(response.content).decode()
        
        print("test")
        print("HOT RLOAD")

        return OutputModel(
            message=message,
            output_file_path=output_file_path,
            image_data=image_data
        )

