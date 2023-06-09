import boto3

session = boto3.Session(
aws_access_key_id='Your Access Key ID',
aws_secret_access_key='You Secret access key'
)

s3 = session.resource('s3')

#Create a Soucre Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
copy_source = {
    'Bucket': 'your_source_bucket_name',
    'Key': 'Object_Key_with_file_extension'
}

bucket = s3.Bucket('target_bucket_name')

bucket.copy(copy_source, 'target_object_name_with_extension')


# Printing the Information That the File Is Copied.
print('Single File is copied')