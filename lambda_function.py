import boto3

import pprint

REGION = "us-east-1"

def stop_instance(instance_id):
  
  print("Stopping instances: {}".format(instance_id))
  ec2.stop_instances(InstanceIds=[instance_id])
  
    
def start_instance(instance_id):
  
  print("Starting instances: {}".format(instance_id))
  ec2.start_instances(InstanceIds=[instance_id])
    
def reboot_instance(instance_id):
  
  print("Rebooting instances: {}".format(instance_id))
  ec2.reboot_instances(InstanceIds=[instance_id])

def lamda_handler(event,context):

  ec2 = boto3.client('ec2',
                      region_name= REGION,
                    )

  instances = ec2.describe_instances(Filters=[{'Name':'tag:Project','Values':['terraform']},
                                            {'Name':'tag:Env','Values':['dev']}])

  for instance in instances['Reservations']:
    
    instance_id = instance['Instances'][0]['InstanceId']
  
    stop_instance(instance_id)
