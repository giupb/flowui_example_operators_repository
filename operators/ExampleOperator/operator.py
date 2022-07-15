from email import message
from flowui.base_operator import BaseOperator
from .models import InputModel, OutputModel


class ExampleOperator(BaseOperator):

    def operator_function(self, input_model: InputModel):
        # The BaseOperator class provides a set of convenience self variables ready to be used
        # to get the unique id for this task run
        self.run_id
        
        # to get the base path where files generated by this task run should be stored
        self.results_path

        # a dict containing xcom data from upstream tasks
        self.upstream_tasks
        
        # a dict containing airflow context data
        self.airflow_context
        
        # a method that allows for logging messages on this task run log
        self.logger

        # to push results to XCom, to be used by other Operators, return an instantiated OutputModel
        return OutputModel(
            message="Task successfully completed!",
            output_arg_1="something else"
        )