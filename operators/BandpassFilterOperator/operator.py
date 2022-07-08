from flowui.base_operator import BaseOperator
from .model import OperatorModel

import os
import spikeinterface.core as sc
import spikeinterface.toolkit as st
import spikeinterface.widgets as sw


class BandpassFilterOperator(BaseOperator):

    def operator_function(self, operator_model: OperatorModel):
        ########## Operator task ##########
        upstream_task_id = list(self.upstream_tasks.keys())[0]
        previous_task_results_path = self.upstream_tasks[upstream_task_id]["results_path"]

        # Load dataset with SpikeInterface Extractor
        rec = sc.load_extractor(previous_task_results_path)
        self.logger.info("Dataset successfully loaded!")

        # Apply band pass filter
        recording_lfp = st.preprocessing.bandpass_filter(
            rec, 
            freq_min=operator_model.freq_min, 
            freq_max=operator_model.freq_max
        )
        self.logger.info(f"Sampling frequency AP: {rec.get_sampling_frequency()}")
        self.logger.info(f"Sampling frequency LF: {recording_lfp.get_sampling_frequency()}")   
    
        # Save results
        recording_lfp.save_to_folder(folder=self.results_path)
        self.logger.info("Band pass successfully applied!")

        ########## Report task ##########
        if operator_model.include_results_in_report:
            self.generate_report(rec=rec, recording_lfp=recording_lfp)

        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "message": "Band pass successfully applied!",
            "other_custom_info": dict()
        }
        return xcom_obj


    def generate_report(self, rec, recording_lfp):
        if not os.path.exists(self.report_path):
            os.makedirs(self.report_path)

        f = open(f"{self.report_path}/text.txt", "a")
        f.write(f"Sampling frequency AP: {rec.get_sampling_frequency()}\n")
        f.write(f"Sampling frequency LF: {recording_lfp.get_sampling_frequency()}")
        f.close()

        w_ts = sw.plot_timeseries(recording_lfp)
        w_ts.figure.savefig(f"{self.report_path}/figure.png")

        self.logger.info("Report docs successfully created!")