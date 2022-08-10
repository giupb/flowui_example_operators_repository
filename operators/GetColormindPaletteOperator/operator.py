from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel

import requests
from pathlib import Path
from io import BytesIO
from PIL import Image
import numpy as np
import json
import base64


class GetColormindPaletteOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        # Read image from results path or from XCOM data
        if input_model.input_file_path:
            img_path = str(Path(input_model.input_file_path).resolve())
            img = Image.open(img_path)
        elif input_model.input_image_data:
            img = Image.open(BytesIO(base64.b64decode(input_model.input_image_data)))
        img_array = np.array(img)
        img_reshaped = str(img_array.reshape((40000, 3)).tolist())

        # Get pallete
        data = '{"input":' + img_reshaped + ',"model":"default"}'
        response = requests.post('http://colormind.io/api/', data=data)
        palette = {
            "palette": response.json()["result"]
        }

        if input_model.save_as_file:
            # Save palette as json
            json_object = json.dumps(palette, indent = 4)
            output_palette_file_path = Path(self.results_path) / "palette.json"
            with open(output_palette_file_path, "w") as f:
                f.write(json_object)
            message = f"Palette successfully generated and saved as file at: {output_palette_file_path}"
            output_palette_data = None
        else:
            # Return palette as XCOM data
            message = "Palette successfully generated and returned as data in XCOM."
            output_palette_file_path = None
            output_palette_data = str(palette)

        return OutputModel(
            message=message,
            output_palette_file_path=str(output_palette_file_path),
            output_palette_data=output_palette_data
        )

