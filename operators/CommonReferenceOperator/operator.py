from flowui.base_operator import BaseOperator
from .model import OperatorModel
from .metadata import metadata

import os
import spikeinterface.core as sc
import spikeinterface.toolkit as st
import spikeinterface.widgets as sw


class CommonReferenceOperator(BaseOperator):

    BaseOperator.set_metadata(metadata=metadata)

    def operator_function(self, operator_model: OperatorModel):
        ########## Operator task ##########
        upstream_task_id = list(self.upstream_tasks.keys())[0]
        previous_task_results_path = self.upstream_tasks[upstream_task_id]["results_path"]

        # Load dataset with SpikeInterface Extractor
        rec = sc.load_extractor(previous_task_results_path)
        self.logger.info("Dataset successfully loaded!")

        # Apply common reference
        recording_processed = st.preprocessing.common_reference(
            rec, 
            reference='global', 
            operator=operator_model.reference_operator
        )
    
        # Save results
        recording_processed.save_to_folder(folder=self.results_path)
        self.logger.info("Common reference successfully applied!")

        ########## Report task ##########
        if operator_model.include_results_in_report:
            self.generate_report(recording_processed=recording_processed)

        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "message": "Band pass successfully applied!",
            "other_custom_info": dict()
        }
        return xcom_obj

    def generate_report(self, recording_processed):
        if not os.path.exists(self.report_path):
            os.makedirs(self.report_path)

        f = open(f"{self.report_path}/text.txt", "a")
        f.write("Some description")
        f.close()

        w_ts = sw.plot_timeseries(recording_processed)
        w_ts.figure.savefig(f"{self.report_path}/figure.png")
