""" 
Inspired by: https://www.youtube.com/watch?v=j65W-L-gQs4&ab_channel=JustinStolpe
https://github.com/jstolpe/blog_code/blob/master/instagram_graph_api/python/posting_content.py 
https://developers.facebook.com/docs/instagram-api/
"""
from flowui.base_operator import BaseOperator
from .model import OperatorModel


class PostInstagramOperator(BaseOperator):

    def operator_function(self, operator_model: OperatorModel):
        # Load image downloaded with previous task
        upstream_task_id = list(self.upstream_tasks.keys())[0]
        previous_task_results_path = self.upstream_tasks[upstream_task_id]["results_path"]

        

        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "message": "Photo successfully posted on Instagram",
        }
        return xcom_obj