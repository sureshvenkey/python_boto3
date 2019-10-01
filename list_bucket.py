import boto3
s3_res=boto3.resource("s3",aws_access_key_id="AKIAJZKRSWXKFQ5KDI4Q", aws_secret_access_key="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", region_name="ap-south-1")
for each_bucket in s3_res.buckets.all():
	print (each_bucket.name)

