# AWS_YouTube_Data_Analysis
For this project, we need the following tools:
1.	AWS S3
2.	AWS IAM
3.	AWS GLUE
4.	AWS LAMBDA
5.	AWS ATHENA

1.	Initially, we need to get a personalized User Credentials using IAM Management Console
2.	Download the dataset from link:	
3.	We created a bucket at S3 and likewise install AWS S2-Client on your computer. You can upload the json and files onto S3 using:
aws s3 cp . s3://bucketname/sub-folder1/sub-folder2/ --recursive --exclude "*" --include"*.json"

aws s3 cp CAvideos.csv s3://bucketname/sub-folder1/ sub-folder2/region=ca/


aws s3 cp DEvideos.csv s3://bucketname/sub-folder1/ sub-folder2/region=de/


aws s3 cp FRvideos.csv s3://bucketname/sub-folder1/ sub-folder2/region=fr/


aws s3 cp GBvideos.csv s3://bucketname/sub-folder1/ sub-folder2/region=gb/


aws s3 cp INvideos.csv s3:// bucketname/sub-folder1/ sub-folder2/region=in/


aws s3 cp JPvideos.csv s3:// bucketname/sub-folder1/ sub-folder2/region=jp/


aws s3 cp KRvideos.csv s3://bucketname/sub-folder1/ sub-folder2/region=kr/


aws s3 cp MXvideos.csv s3:// bucketname/sub-folder1/ sub-folder2/region=mx/


aws s3 cp RUvideos.csv s3:// bucketname/sub-folder1/ sub-folder2/region=ru/


aws s3 cp USvideos.csv s3:// bucketname/sub-folder1/ sub-folder2/region=us/

4.	Create a crawler at AWS Glue to add/update tables in the Glue.
5.	Use AWS Lambda to normalize the items in the json file using codes at lambda_function.py
6.	Once the datafile gets in a proper format, you can perform query using SQL Athena
