'''
Delete available and untagged volumes using python filter
Created on 02-Oct-2019

@author: venkatraj
'''
import boto3
from pprint import pprint
sess=boto3.session.Session(profile_name="default")
ec2_res=sess.resource(service_name="ec2", region_name="ap-south-1")
ec2_cli=sess.client(service_name="ec2", region_name="ap-south-1") # Used for waiters
#To print all volumes
print ("List all volumes \nVolume_ID Volume_Status Volume_Tag")
for each_ec2_vol in ec2_res.volumes.all():
    print (each_ec2_vol.id, each_ec2_vol.state, each_ec2_vol.tags)
#Delete available and untagged volumes
for each_ec2_vol in ec2_res.volumes.all():
    if each_ec2_vol.state == 'available' and each_ec2_vol.tags == None:
        ec2_res.Volume(each_ec2_vol.id).delete()
        try:
            waiter = ec2_cli.get_waiter('volume_deleted')
            waiter.wait(VolumeIds=[each_ec2_vol.id])
            print ("\n"+ each_ec2_vol.id +" volume deleted")
        except Exception as e:
            print (e) 
