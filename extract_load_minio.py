'''
Author: Jason
Topic: To extract file from website and load to minio bucket
Date: Oct, 2023

'''

import requests
from minio import Minio
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
import logging
import pandas as pd
from io import BytesIO
from creds import minio_endpoint,minio_access_key,minio_secret_key,minio_bucket_name,minio_file_name
from load_to_bq import extract_files_from_minio 


# Configure logging
logging.basicConfig(filename='upload.log', level=logging.INFO)

def get_files(URL_DATA):

    # Send a GET request to the URL and download the file
    response = requests.get(URL_DATA)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the downloaded file
        with open('ridership_headline.csv', 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully.")

        df_final = pd.read_csv('ridership_headline.csv')

        # data manipulations or analysis on the DataFrame
        # print the first few rows
        print(df_final.head(5))

    else:
        print("Failed to download the file.")

    load_minio(df_final)

def load_minio(df_final):
    # Initialize MinIO client
    minio_client = Minio(
        minio_endpoint,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=False  # Change to True if using HTTPS
    )

    data_bytes = df_final.to_csv().encode('utf-8')
    data_buffer = BytesIO(data_bytes)

    minio_client.put_object(
        bucket_name=minio_bucket_name,
        object_name=minio_file_name,
        data=data_buffer,
        length=len(data_bytes),
        content_type="application/csv"  # Adjust content type as needed
    )
    logging.info("File successfully loaded into MinIO.")

    extract_files_from_minio()


if __name__ == '__main__':
    URL_DATA = 'https://storage.data.gov.my/transportation/ridership_headline.csv'
    get_files(URL_DATA)
