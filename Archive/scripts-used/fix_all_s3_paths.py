#!/usr/bin/env python3
import boto3
import sys
import io

if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

s3 = boto3.client('s3')
bucket = 'isnbiz-assets-1769962280'

print("Fixing ALL S3 paths...")
fixed = 0
errors = 0

paginator = s3.get_paginator('list_objects_v2')

for page in paginator.paginate(Bucket=bucket):
    if 'Contents' not in page:
        continue

    for obj in page['Contents']:
        key = obj['Key']

        if '\\' in key:
            new_key = key.replace('\\', '/')
            print(f"{key} -> {new_key}")

            try:
                s3.copy_object(
                    Bucket=bucket,
                    CopySource={'Bucket': bucket, 'Key': key},
                    Key=new_key
                )
                s3.delete_object(Bucket=bucket, Key=key)
                fixed += 1
            except Exception as e:
                print(f"Error: {e}")
                errors += 1

print(f"\nFixed {fixed} files, {errors} errors")
