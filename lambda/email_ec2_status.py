import json
import boto3

def lambda_handler(event, context):
    # TODO implement
   
    ec2_res=boto3.resource(service_name="ec2", region_name="ap-south-1")
    sns_cli=boto3.client(service_name="sns", region_name="ap-south-1")
    #print("Received event: " + json.dumps(event['detail']['instance-id'], indent=2))
    instance_name = event['detail']['instance-id']
    message = instance_name + " Instance is in stopped state"
    print(message)
    sns_cli.publish(TargetArn="arn:XXX:XXX:XXXXXXX:XXXXXXXXX:XXXXXXXXXXXXXXXXXXX",
    Message=message,
    Subject="Ec2 Instance State")
   

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
