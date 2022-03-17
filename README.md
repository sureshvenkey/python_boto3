## Automation with boto3
### Getting Started
boto3 is a python module that allows you to automat aws services, which can be used with aws lambda to create a serverless application.
### Prerequisite  
1. Python 3.7.4
2. aws-cli
>pip install awscli --user
3. boto3
>pip install boto3 --user
### Configuring awscli credencials
Steps to configure aws credencials  
C:\Users\venkatraj\Desktop\boto3>pip install awscli --user  
C:\Users\venkatraj\Desktop\boto3>aws configure  
AWS Access Key ID [None]: XXXXXXXXXXXXXXXXXXXXXX  
AWS Secret Access Key [None]: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  
Default region name [None]: ap-south-1  
Default output format [None]: json  
C:\Users\venkatraj\Desktop\boto3>  

### Code  
Code Name | Description
----------|-------------
del_unused_vol.py | Deletes unused volumes for a specific region i.e. volume unassigned with any ec2 instance with no tags.
del_unused_vol_region.py | Deletes unused volumes  for all region i.e. volume unassigned with any ec2 instance with no tags.
inventory_ec2_vol_sg.py | Creates a inventory in the form of csv file in the current location for ec2 instances, volumes and security group for a specified region.
list_ec2_volumes_with_boto3_filters.py | How to use boto3 filter for tags
list_ec2_volumes_with_default_filters.py | How to use default filter for tags, helpfull in deleting volumes where key=value pair not matching tags.
tag_ec2_vol_csv.py | Tag volumes based on csv input file, csv file format, "Volume_ID","Key","Value" The script check whether same key=value pair available in in volume tags and tages volumes. If same key is available with change in value, then the script modifies the tag. 

### License
GNU General Public License v3.0  
Mail Me: sureshvenkey@gmail.com  
Website: www.venkatraj.in


