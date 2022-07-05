from flowuipackage.base_operator import BaseOperator
from .model import OperatorModel

import requests
from pathlib import Path
from io import BytesIO
from PIL import Image


class DownloadImageOperator(BaseOperator):

    def operator_function(self, operator_model: OperatorModel):
        # Request random image
        response = requests.get(f'https://picsum.photos/{operator_model.width_pixels}/{operator_model.height_pixels}')
        img = Image.open(BytesIO(response.content))

        image_path = Path(self.results_path) / "image.jpeg"
        if not Path(self.results_path).is_dir():
            Path(self.results_path).mkdir(parents=True, exist_ok=True)
        img.save(fp=image_path)
        self.logger.info("Image downloaded")

        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "message": f"Image successfully downloaded to: {image_path}",
            "other_custom_info": dict(
                image_path=str(image_path)
            )
        }
        return xcom_obj

