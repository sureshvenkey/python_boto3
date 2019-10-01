import boto3
sess=boto3.session.Session(profile_name="default")
s3_res=sess.resource(service_name="s3", region_name="ap-south-1")
for each_bucket in s3_res.buckets.all():
	print (each_bucket.name)



