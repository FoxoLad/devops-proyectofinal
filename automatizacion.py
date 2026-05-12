import boto3
from datetime import datetime, timezone, timedelta

# Configuration
REGION = 'us-east-1'

print("===================================")
print(" AWS Automation Script")
print("===================================\n")

# Use a session to share configuration across clients
session = boto3.Session(region_name=REGION)
ec2 = session.client('ec2')
cloudwatch = session.client('cloudwatch')
s3 = session.client('s3')
autoscaling = session.client('autoscaling')

# =========================
# EC2 INSTANCES
# =========================
print("Listing EC2 Instances...\n")
instance_ids = []
ec2_paginator = ec2.get_paginator('describe_instances')

for page in ec2_paginator.paginate():
    for reservation in page['Reservations']:
        for instance in reservation['Instances']:
            i_id = instance['InstanceId']
            i_type = instance['InstanceType']
            state = instance['State']['Name']
            
            instance_ids.append(i_id)
            
            print(f"ID: {i_id}")
            print(f"Type: {i_type}")
            print(f"State: {state}")
            print("-----------------------------")

# =========================
# CLOUDWATCH METRICS
# =========================
print("\nGetting CPU metrics (Last 24h)...\n")
end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(hours=24)

for instance_id in instance_ids:
    metrics = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=start_time,
        EndTime=end_time,
        Period=3600,
        Statistics=['Average']
    )
    
    print(f"CPU Metrics for {instance_id}")
    datapoints = metrics.get('Datapoints', [])

    if datapoints:
        # Sort by timestamp so the output makes sense
        datapoints = sorted(datapoints, key=lambda x: x['Timestamp'])
        for point in datapoints:
            print(f"Time: {point['Timestamp']}")
            print(f"Average CPU: {point['Average']:.2f}%")
            print("-----------------------------")
    else:
        print("No CPU data available.")
        print("-----------------------------")

# =========================
# S3 BUCKETS
# =========================
print("\nListing S3 Buckets...\n")
buckets = s3.list_buckets()
s3_paginator = s3.get_paginator('list_objects_v2')

for bucket in buckets['Buckets']:
    bucket_name = bucket['Name']
    print(f"Bucket: {bucket_name}")

    try:
        for page in s3_paginator.paginate(Bucket=bucket_name):
            if 'Contents' in page:
                for obj in page['Contents']:
                    print(f" - {obj['Key']}")
            else:
                print(" - No objects found")
    except Exception as e:
        print(f" - Error accessing bucket: {e}")
    print("-----------------------------")

# =========================
# AUTO SCALING GROUPS
# =========================
print("\nListing Auto Scaling Groups...\n")
asg_paginator = autoscaling.get_paginator('describe_auto_scaling_groups')

for page in asg_paginator.paginate():
    for group in page['AutoScalingGroups']:
        print(f"Name: {group['AutoScalingGroupName']}")
        print(f"Min Size: {group['MinSize']}")
        print(f"Max Size: {group['MaxSize']}")
        print(f"Desired Capacity: {group['DesiredCapacity']}")
        print("-----------------------------")

print("\nAutomation script completed.")
