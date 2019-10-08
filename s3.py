# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:11:31 2019

@author: user
"""
import boto3
import botocore
import pandas as pd

BUCKET_NAME = 'blossom-data-engs'
KEY = 'free-7-million-company-dataset.zip'

s3 = boto3.client('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, 'my_free-7-million-company-dataset.zip')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

# read with pandas  
df = pd.read_csv('my_free-7-million-company-dataset.zip')

# setting na_values
df = pd.read_csv('my_free-7-million-company-dataset.zip', na_values = {
    'domain': ["not available", "n.a", "n.a."})
                 
#filter off companies with empty domain 
df = df.dropna(subset = ['domain'])

#writing to parquet format 
df.to_parquet('my_free-7-million-company-dataset.parquet.gzip', compression='gzip')
                 
#writing to json format
df.to_json(r'my_free-7-million-company-dataset.json')


s3.upload_file('s3.py', 'blossom-data-eng-justice-akwensi', 'free-7-million-company-dataset-json.gzip')

s3.upload_file('s3.py', 'blossom-data-eng-justice-akwensi', 'my_free-7-million-company-dataset.parquet.gzip')
