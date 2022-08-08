
# Lamda_Function_to_Modify_ec2_instace_state
Lambda function to start stop and reboot


## Usage

- The lambda function can be triggered using cloud watch events to schedule start, stop or reboot of amazon ec2-instances.
- The functions that can be user with the lambda function are:

```python
def stop_instance(instance_id):
  
  print("Stopping instances: {}".format(instance_id))
  ec2.stop_instances(InstanceIds=[instance_id])
  
    
def start_instance(instance_id):
  
  print("Starting instances: {}".format(instance_id))
  ec2.start_instances(InstanceIds=[instance_id])
    
def reboot_instance(instance_id):
  
  print("Rebooting instances: {}".format(instance_id))
  ec2.reboot_instances(InstanceIds=[instance_id])

```
- The main lamda_handler function:
```python
def lamda_handler(event,context):

  ec2 = boto3.client('ec2',
                      region_name= REGION,
                    )

  instances = ec2.describe_instances(Filters=[{'Name':'tag:Project','Values':['terraform']},
                                            {'Name':'tag:Env','Values':['dev']}])

  for instance in instances['Reservations']:
    
    instance_id = instance['Instances'][0]['InstanceId']
  
    stop_instance(instance_id)
   #start_instance(instance_id) 
   #reboot_instance(instance_id)
```
- Set the event on the Cloud watch events to trigger the lambda function.
- Do not forget to attach the role with appropriate policy to the lambda function
