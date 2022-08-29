import requests
from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel
import json


class ExampleOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        # The BaseOperator class provides a set of convenience self variables ready to be used
        secret_msg = f"""
        Example Operator secret: {self.secrets}
        """
        self.logger.info(secret_msg)

        url = "https://airbnb19.p.rapidapi.com/api/v1/searchPropertyByPlace"
        querystring = {"id":"ChIJN3P2zJlG0i0RACx9yvsLAwQ", "totalRecords":"20", "currency":"USD", "adults":"1"}
        headers = {
            "X-RapidAPI-Key": self.secrets.get('API_KEY'),
            "X-RapidAPI-Host": "airbnb19.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_dict = json.loads(response.text)

        output = []
        for e in response_dict.get('data'):
            aux = {
                "rate": float(e.get('avgRating')),
                "beds": e.get('beds'),
                "city": e.get('city'),
                "price": e.get('price')
            }
            output.append(aux)
        output = sorted(output, key=lambda d: d['rate'], reverse=True)

        self.logger.info(output)
        return OutputModel(
            data=output,
            message="Task completed"
        )