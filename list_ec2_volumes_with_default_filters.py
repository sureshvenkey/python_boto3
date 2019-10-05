'''
List ec3 volumes with default python filters
Created on 02-Oct-2019

@author: venkatraj
'''
import boto3
from pprint import pprint
sess=boto3.session.Session(profile_name="default")
ec2_res=sess.resource(service_name="ec2", region_name="ap-south-1")

for each_ec2_vol in ec2_res.volumes.all():
	print (each_ec2_vol.id, each_ec2_vol.state, each_ec2_vol.tags)
print ("\n")
vol_filter=[{'Name':'status','Values':['available']}]
for each_ec2_vol in ec2_res.volumes.filter(Filters=vol_filter):	
	if each_ec2_vol.tags != None:
		if not any(d['Key'] == 'DND' and d['Value'] == 'No' for d in each_ec2_vol.tags):
			print ("Not Available tag DNS=No --> "+ each_ec2_vol.id, each_ec2_vol.state, each_ec2_vol.tags)
		else:
			print ("Available tag DNS=No--> "+ each_ec2_vol.id, each_ec2_vol.state, each_ec2_vol.tags)
for each_ec2_vol in ec2_res.volumes.filter(Filters=vol_filter):	
	if each_ec2_vol.tags == None:
		print ("Not Available tag DNS=No --> "+ each_ec2_vol.id, each_ec2_vol.state, each_ec2_vol.tags)
