from flowui.base_operator import BaseOperator
from flowui.client.s3_client import S3Client
from .model import OperatorModel

import os
import spikeinterface.extractors as se
import spikeinterface.widgets as sw


class LoadSpikeglxOperator(BaseOperator):

    def operator_function(
        self,
        operator_model: OperatorModel
    ):
        ########## Operator task ##########
        # Set S3 client
        s3_client = S3Client(bucket_name=operator_model.bucket_name)

        # Set volume path for dataset
        dataset_id = operator_model.dataset_path.split('/')[-2] if operator_model.dataset_path[-1] == '/' else operator_model.dataset_path.split('/')[-1]
        dataset_path_fs = f"{self.volume_mount_path}/datasets/{dataset_id}/"

        # Check if artifact already exists, before copying it from S3
        if os.path.exists(dataset_path_fs):
            self.logger.info(f"The {dataset_id} dataset already exists!")
        else:    
            # Copy dataset from S3 to File System
            err = s3_client.download_s3_folder(
                s3_folder=f"datasets/{dataset_id}/", 
                local_dir=dataset_path_fs
            )
            if err is None:
                self.logger.info(f"Dataset {dataset_id} successfully downloaded!")
            else:
                self.logger.error(err)

        # Read dataset with SpikeInterface Extractor and save as Binary
        rec = se.SpikeGLXRecordingExtractor(
            folder_path=dataset_path_fs, 
            stream_id=f"imec.{operator_model.stream_id}"
        )

        # Uncomment the line below to use only 5% of the data
        # rec = rec.frame_slice(start_frame=0, end_frame=int(rec.get_num_frames()*0.05))
    
        rec.save_to_folder(folder=self.results_path)

        self.logger.info(f"Num channels: {rec.get_num_channels()}")
        self.logger.info(f"Sampling rate: {rec.get_sampling_frequency()}")
        self.logger.info(f"Duration (s): {rec.get_num_frames() / rec.get_sampling_frequency()}")
        self.logger.info(f"Dataset transformed to SI binary format and stored at: {self.results_path}")

        ########## Report task ##########
        if operator_model.include_results_in_report:
            self.generate_report(rec=rec)
        
        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "results_message": "SI extractor data successfully loaded to EFS!",
            "other_custom_info": dict()
        }
        return xcom_obj


    def generate_report(self, rec):
        if not os.path.exists(self.report_path):
            os.makedirs(self.report_path)

        f = open(f"{self.report_path}/text.txt", "a")
        f.write(f"Num channels: {rec.get_num_channels()}\n")
        f.write(f"Sampling rate: {rec.get_sampling_frequency()}\n")
        f.write(f"Duration (s): {rec.get_num_frames() / rec.get_sampling_frequency()}")
        f.close()

        w_ts = sw.plot_timeseries(rec)
        w_ts.figure.savefig(f"{self.report_path}/figure.png")