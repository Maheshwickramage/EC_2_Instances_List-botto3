import boto3

# Initialize EC2 client
ec2 = boto3.client('ec2')

# Function to terminate any running EC2 instances and list them

def list_and_stop_instances():
    # Obtain every instance that is currently operating.

    instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    # Go over each case in turn.

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_state = instance['State']['Name']
            print(f"Instance ID: {instance_id}, State: {instance_state}")

            # If the instance is running, stop it.
            if instance_state == 'running':
                print(f"Stopping instance {instance_id}...")
                ec2.stop_instances(InstanceIds=[instance_id])
                print(f"Instance {instance_id} stopped.")

# Run the program

list_and_stop_instances()