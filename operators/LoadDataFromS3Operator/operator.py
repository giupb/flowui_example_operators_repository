from flowui.base_operator import BaseOperator
from flowui.client.s3_client import S3Client
from .model import OperatorModel

import os


class LoadDataFromS3Operator(BaseOperator):
    
    def operator_function(self, operator_model: OperatorModel):
        ########## Operator task ##########
        s3_client = S3Client(bucket_name=operator_model.bucket_name)

        # Create mnt dataset path
        dataset_id = operator_model.dataset_path.split('/')[-2] if operator_model.dataset_path[-1] == '/' else operator_model.dataset_path.split('/')[-1]
        dataset_path_fs = f"{self.volume_mount_path}/datasets/{dataset_id}/"

        # Check if artifact already exists, before copying it from S3
        if os.path.exists(dataset_path_fs):
            self.logger.info(f"The {dataset_id} dataset already exists!")
        else:    
            # Copy dataset from S3 to Mount path
            err = s3_client.download_s3_folder(
                s3_folder=f"datasets/{dataset_id}/", 
                local_dir=dataset_path_fs
            )
            if err is None:
                self.logger.info(f"Dataset {dataset_id} successfully downloaded!")
            else:
                self.logger.error(err)
 
        ########## Push results - accessible through XComs ##########
        xcom_obj = {
            "results_message": "Data successfully loaded to File System!",
            "other_custom_info": dict()
        }
        return xcom_obj