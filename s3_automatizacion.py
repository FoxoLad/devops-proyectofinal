import boto3

bucket_name = "devops-bucket-569038358773"

s3 = boto3.client('s3')

print("Creating local test file...")

with open("archivo_prueba.txt", "w") as file:
    file.write("DevOps AWS S3 automation test")

print("Uploading file to S3...")

s3.upload_file(
    "archivo_prueba.txt",
    bucket_name,
    "pruebas/archivo_prueba.txt"
)

print("Listing bucket objects...\n")

objects = s3.list_objects_v2(Bucket=bucket_name)

if 'Contents' in objects:

    for obj in objects['Contents']:

        print(f"Name: {obj['Key']}")
        print(f"Size: {obj['Size']} bytes")
        print(f"Last Modified: {obj['LastModified']}")
        print("-----------------------------")

else:
    print("No objects found.")
