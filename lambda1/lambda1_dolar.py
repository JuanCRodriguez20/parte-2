import json
import boto3
from urllib.request import urlopen

def lambda_handler(event, context):
    with urlopen("https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario") as response:
        body = response.read()
    s3 = boto3.client('s3')
    s3.put_object(Body=body, Bucket='dolar-raw-09',Key='dolar_timestap.txt')
    
    return{
    	'statusCode': 200,
    	'body': json.dumps('Hello from lambda!!!')
    }