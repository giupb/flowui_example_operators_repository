from flowuipackage.base_operator import BaseOperator
from .model import OperatorModel


class LoadOpenephysOperator(BaseOperator):

    def operator_function(
        self,
        operator_model: OperatorModel
    ):
        ########## Operator task ##########
        
        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "results_message": "SI extractor data successfully loaded to FS!",
            "other_custom_info": dict()
        }
        return xcom_obj
