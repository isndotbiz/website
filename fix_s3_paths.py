#!/usr/bin/env python3
"""Fix S3 file paths - copy from backslash to forward slash paths"""
import boto3
import sys

s3 = boto3.client('s3')
bucket = 'isnbiz-assets-1769962280'

print("=== Fixing S3 Paths ===\n")

# List all objects
paginator = s3.get_paginator('list_objects_v2')
pages = paginator.paginate(Bucket=bucket, Prefix='assets/founders')

fixed_count = 0
for page in pages:
    if 'Contents' not in page:
        continue

    for obj in page['Contents']:
        key = obj['Key']

        # Check if key has backslashes
        if '\\' in key:
            new_key = key.replace('\\', '/')
            print(f"Copying: {key} -> {new_key}")

            # Copy object to new key
            s3.copy_object(
                Bucket=bucket,
                CopySource={'Bucket': bucket, 'Key': key},
                Key=new_key
            )
            fixed_count += 1

            # Delete old backslash version
            s3.delete_object(Bucket=bucket, Key=key)

print(f"\n✅ Fixed {fixed_count} files in S3")
print(f"All files now have forward-slash paths")
