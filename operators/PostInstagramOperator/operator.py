""" 
Inspired by: https://www.youtube.com/watch?v=j65W-L-gQs4&ab_channel=JustinStolpe
https://github.com/jstolpe/blog_code/blob/master/instagram_graph_api/python/posting_content.py 
https://developers.facebook.com/docs/instagram-api/
"""
from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel


class PostInstagramOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        # Load image downloaded with previous task
        img_path = input_model.input_image_path

        # Post on instagram

        
        return OutputModel(
            message="Photo successfully posted on Instagram"
        )