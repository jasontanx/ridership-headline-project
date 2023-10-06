'''
Author: Jason
Topic: To extract file from minio bucket and ingest into bigquery table
Date: Oct, 2023

'''

from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
from minio import Minio
import pandas as pd
from io import BytesIO

import time
import logging
from creds import minio_endpoint,minio_access_key,minio_secret_key,minio_bucket_name,minio_file_name

project_id = 'myfirstproject-364809'
dataset_id = 'ridership_headline'
tbl_id = 'ridership_headline_v1'

key_path = "key.json"

def get_logging_format() -> logging.Logger:
    """
    function to return custom format logging

    return logging.Logger
    """

    logging.Formatter.converter = time.gmtime
    logging.basicConfig(
        format="[%(asctime)s,%(msecs)d] %(levelname)-8s [%(filename)s:%(lineno)d] - %(message)s",
        datefmt="%Y-%m-%d, %H:%M:%S",
        level=logging.INFO,
    )
    _logger: logging.Logger = logging.getLogger("de-logging")
    return _logger

logger: logging.Logger = get_logging_format()


def extract_files_from_minio():

    print("this block is running")

    try:

        minio_client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False  # Change to True if using HTTPS
    )
        # Retrieve data from MinIO
        minio_data = minio_client.get_object(
            bucket_name=minio_bucket_name,
            object_name=minio_file_name,
        )
        
        # Read the MinIO data into a DataFrame (assuming it's CSV)
        df = pd.read_csv(BytesIO(minio_data.read()))

    except Exception as e:
        print(f"Failed to load data into BigQuery: {e}")

    load_bq(df)

def load_bq(df):

    logger.info("ingesting to bq...")
    bq_client = bigquery.Client.from_service_account_json(key_path) # Initialize BigQuery client
    table_bq = f'{project_id}.{dataset_id}.{tbl_id}'
    job_config = bigquery.LoadJobConfig()
    job_config.write_disposition="WRITE_TRUNCATE" # "WRITE_APPEND" as alternative
    job = bq_client.load_table_from_dataframe(
        df, table_bq, job_config=job_config)
    job.result()
    logger.info("Data ingested to BQ -> %s", table_bq)
