from flowuipackage.base_operator import BaseOperator
from .model import OperatorModel

import requests
from pathlib import Path
from PIL import Image
import numpy as np
import json


class DownloadImageOperator(BaseOperator):

    def operator_function(self, operator_model: OperatorModel):
        # Load local image - downloaded with previous task
        upstream_task_id = list(self.upstream_tasks.keys())[0]
        previous_task_results_path = self.upstream_tasks[upstream_task_id]["results_path"]

        img_path = Path(previous_task_results_path) / "image.jpeg"
        img = Image.open(img_path)
        img_array = np.array(img)
        img_reshaped = str(img_array.reshape((40000, 3)).tolist())

        # Get pallete
        data = '{"input":' + img_reshaped + ',"model":"default"}'
        response = requests.post('http://colormind.io/api/', data=data)
        palette = {
            "palette": response.json()["result"]
        }

        # Save palette as json
        json_object = json.dumps(palette, indent = 4)
        palette_path = Path(self.results_path) / "palette.json"
        with open(palette_path, "w") as f:
            f.write(json_object)

        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "message": f"Palette successfully saved to: {palette_path}",
            "other_custom_info": dict(
                palette_path=str(palette_path)
            )
        }
        return xcom_obj
