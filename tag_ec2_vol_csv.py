'''
Tag volumes based on csv input file, csv file format,
Volume_ID,Key,Value

The script check whether same key=value pair available in in volume tags
and tages volumes. If same key is available with change in value, then
the script modifies the tag. 

Created on 02-Oct-2019

@author: venkatraj
'''
import boto3
import csv
from pprint import pprint
sess=boto3.session.Session(profile_name="default")
ec2_res=sess.resource(service_name="ec2", region_name="ap-south-1")
ec2_cli=sess.client(service_name="ec2", region_name="ap-south-1") # Used for waiters
    
inpfile=open("vol_tag_input.csv","rt")
csv_r=csv.reader(inpfile)
for row in csv_r:
    ec2_vol = ec2_res.Volume(row[0])
    print ("Before:", ec2_vol.id, ec2_vol.state, ec2_vol.tags)
    if ec2_vol.tags == None:
        ec2_vol.create_tags(Tags=[{'Key': row[1], 'Value': row[2]}])
        print ("Tag added in "+row[0])
        print ("After:", ec2_vol.id, ec2_vol.state, ec2_vol.tags)
    elif not any(d['Key'] == row[1] and d['Value'] == row[2] for d in ec2_vol.tags):
        ec2_vol.create_tags(Tags=[{'Key': row[1], 'Value': row[2]}])
        print ("Tag added in "+row[0])
        print ("After:", ec2_vol.id, ec2_vol.state, ec2_vol.tags)
    else:
        print ("Tag already added in "+row[0])
        print ("After:", ec2_vol.id, ec2_vol.state, ec2_vol.tags)
