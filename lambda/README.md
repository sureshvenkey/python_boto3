
## Automation with lambda & boto3
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

### Procedure for executing lambda  

1. Create a IAM role for lambda ( here lambda is the Trusted entitie) with two policies attached to it "AmazonEC2FullAccess" and "AmazonSNSFullAccess". Here we have given full access, you can restrict if you wish. 
2. Create a lambda function by 


Code Name | Description
----------|-------------
email_ec2_status.py | Sends mail alert if an instance is reached to shutdown state.


### License
GNU General Public License v3.0  
Mail Me: sureshvenkey@gmail.com  
Website: www.sureshvenkey.com


