from flowui.base_operator import BaseOperator
from .model import OperatorModel

import os
import spikeinterface.extractors as se
import spikeinterface.widgets as sw


class ToyDatasetOperator(BaseOperator):

    def operator_function(self, operator_model: OperatorModel):
        ########## Operator task ##########
        # Create Toy example
        recording, sorting = se.toy_example(
            duration=operator_model.duration, 
            num_channels=operator_model.num_channels, 
            num_units=operator_model.num_units,
            sampling_frequency=operator_model.sampling_frequency,
            num_segments=1, # TODO segment index
            average_peak_amplitude=operator_model.average_peak_amplitude,
            upsample_factor=operator_model.upsample_factor,
            contact_spacing_um=operator_model.contact_spacing_um,
            num_columns=operator_model.num_columns,
            seed=operator_model.seed
        )

        # Save dataset to EFS
        recording.save_to_folder(folder=self.results_path)
        sorting.save_to_folder(folder=self.results_path + "/sorting")

        self._logger.info(f"Num channels: {recording.get_num_channels()}")
        self._logger.info(f"Sampling rate: {recording.get_sampling_frequency()}")
        self._logger.info(f"Toy dataset {operator_model.dataset_id} successfully created and stored at {self.results_path}!")

        ########## Report task ##########
        if operator_model.include_results_in_report:
            self.generate_report(recording=recording)
        
        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "message": f"Toy dataset {operator_model.dataset_id} successfully created and stored at {self.results_path}!",
            "other_custom_info": dict()
        }
        return xcom_obj

    def generate_report(self, recording):
        if not os.path.exists(self.report_path):
            os.makedirs(self.report_path)

        f = open(f"{self.report_path}/text.txt", "a")
        f.write(f"Num channels: {recording.get_num_channels()}\n")
        f.write(f"Sampling rate: {recording.get_sampling_frequency()}\n")
        f.close()

        w_ts = sw.plot_timeseries(recording) # TODO segment index
        w_ts.figure.savefig(f"{self.report_path}/figure.png")
