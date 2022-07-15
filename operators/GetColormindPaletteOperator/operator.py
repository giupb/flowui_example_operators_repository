from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel

import requests
from pathlib import Path
from PIL import Image
import numpy as np
import json


class GetColormindPaletteOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        img_path = str(Path(input_model.input_file_path).resolve())
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

        return OutputModel(
            message="Palette successfully generated!",
            output_palette_path=str(palette_path)
        )

