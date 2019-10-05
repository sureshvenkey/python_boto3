'''
List ec3 volumes with boto3 filters
Created on 02-Oct-2019

@author: venkatraj
'''
import boto3
from pprint import pprint
sess=boto3.session.Session(profile_name="default")
ec2_res=sess.resource(service_name="ec2", region_name="ap-south-1")

print ("Print all volumes")
for each_ec2_vol in ec2_res.volumes.all():
	print (each_ec2_vol.id,each_ec2_vol.state,each_ec2_vol.tags)

print ("\nPrint volumes with available status and where tag DND is Yes")
vol_filter=[{'Name':'status', 'Values':['available']},{'Name':'tag:DND', 'Values':['Yes']}]
for each_ec2_vol in ec2_res.volumes.filter(Filters=vol_filter):
	print (each_ec2_vol.id,each_ec2_vol.state, each_ec2_vol.tags)

print ("\nPrint volumes with available status and where tag Name is mentioned, here Name is the tag")
vol_filter=[{'Name':'status', 'Values':['available']},{'Name':'tag-key', 'Values':['Name']}]
for each_ec2_vol in ec2_res.volumes.filter(Filters=vol_filter):
	print (each_ec2_vol.id,each_ec2_vol.state, each_ec2_vol.tags)
