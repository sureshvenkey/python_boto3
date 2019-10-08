
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
2. Create a lambda function by specifying the function name, runtime(python 3.7).
3. Mention the code in function code section.
3. Select the appropriate IAM role for your function, which we have created now. You can also increase the timeout value in basic section if required, by default it is 3 seconds.
4. Once you have done save the function. 
5. From cloudwatch ceate a "Event Pattern" event source by specifying the filtering criteria, example  
Service Name: EC2  
Event Type: EC2 Instance State-change Notification  
Specific state(s): stopped  
Any instance: Yes  
6. Select the created function to crecive the events from event source by selection it from Traget.
7. We are done we are about to receive the mail if the ec2 state is stopped.




Code Name | Description
----------|-------------
email_ec2_status.py | Sends mail alert if an instance is reached to stopped state.


### License
GNU General Public License v3.0  
Mail Me: sureshvenkey@gmail.com  
Website: www.sureshvenkey.com


