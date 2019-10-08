# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:11:31 2019

@author: user
"""
import boto3
import botocore
import pandas as pd

BUCKET_NAME = 'blossom-data-engs'
KEY = 'project1/free-7-million-company-dataset.zip'

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_free-7-million-company-dataset.zip')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
 
    
df = pd.read_csv('my_free-7-million-company-dataset.zip')

df = df[df['domain'].str.len() == 0]

df.to_json(r'my_free-7-million-company-dataset.json')

df.to_parquet('my_free-7-million-company-dataset.parquet.gzip', compression='gzip')

s3_client.upload_file("my_free-7-million-company-dataset.zip", bucket, "my_free-7-million-company-dataset.zip")