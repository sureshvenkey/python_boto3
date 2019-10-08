'''
Delete available and untagged volumes from all region using python filter
Created on 02-Oct-2019

@author: venkatraj
'''
import boto3
from pprint import pprint
sess=boto3.session.Session(profile_name="default")
ec2_cli=sess.client(service_name="ec2", region_name="ap-south-1") # Used for waiters and list regions
for each_region in [region['RegionName'] for region in ec2_cli.describe_regions()['Regions']]:
    ec2_res=sess.resource(service_name="ec2", region_name=each_region)
    ec2_cli=sess.client(service_name="ec2", region_name=each_region)
    print ("Checking for "+each_region)
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
