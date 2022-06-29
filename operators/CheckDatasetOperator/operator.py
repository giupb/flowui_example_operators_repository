from flowuipackage.base_operator import BaseOperator
from flowuipackage.client.fs_client import FSClient
from .model import OperatorModel
from .metadata import metadata

import os
import spikeinterface
import spikeinterface.widgets as sw


class CheckDatasetOperator(BaseOperator):

    BaseOperator.set_metadata(metadata=metadata)

    def operator_function(self, operator_model: OperatorModel):
        ########## Operator task ##########
        fs_client = FSClient()
        upstream_tasks_processed = []

        if not os.path.exists(self.report_path):
            os.makedirs(self.report_path)

        for upstream_task in list(self.upstream_tasks.keys()):
            previous_task_results_path = self.upstream_tasks[upstream_task]["results_path"]
        
            # Create File System path
            fs_client.create_fs_results_path(results_path_fs=self.results_path)

            # Load SI extractor (contains dataset in binary format)
            rec = spikeinterface.load_extractor(previous_task_results_path)
            self.logger.info(f"Data from {upstream_task} successfully read and checked!")

            upstream_tasks_processed.append(upstream_task)

            ########## Report task ##########
            if operator_model.include_results_in_report:
                self.generate_report(rec=rec, upstream_task=upstream_task)

        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "operator": self.__name__,
            "message": f"{' and '.join(upstream_tasks_processed)} data successfully read and checked!",
            "results_metadata": dict()
        }
        return xcom_obj

    def generate_report(self, rec, upstream_task):
            # Saves a snapshot of the traces in a jpg image
            chs = rec.get_channel_ids()[0:10]
            w_ts = sw.plot_timeseries(rec, channel_ids=chs, time_range=(0, 3), segment_index=0)
            w_ts.figure.savefig(f"{self.report_path}/{str(upstream_task)}_figure.png")
            self._logger.info(f"{upstream_task} figure saved at {self.report_path}!")

