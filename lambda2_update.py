import json
import boto3
from datetime import datetime

def lambda_handler(event, context):
	# TODO implement
	s3 = boto3.resource('s3')
	bucket = s3.Bucket('dolar-raw-09')
	obj = bucket.Object('dolar_timestap.txt')
	body = obj.get()['Body'].read()
	todo_item = json.loads(body)
    
	new_data = 'fecha/hora, valor'
    
	for i in todo_item:
	    new_data += str(datetime.fromtimestamp(int(i[0])/1000))+','+i[1]
    
	s3 = boto3.client('s3')
	s3.put_object(Body=new_data, Bucket='dolar-update',Key='dolar_timestap.csv')
    
	return {
    	'statusCode': 200,
    	'body': json.dumps('Hello from Lambda!')
	}