aws lambda add-permission --function-name arn:aws:lambda:us-east-1:420279361566:function:updateContent-updateContent-4RACAC98G05Q --statement-id api-gateway-invoke --action lambda:InvokeFunction --source-arn arn:aws:execute-api:us-east-1:420279361566:ktj2974nv7/*/POST/doctor --principal apigateway.amazonaws.com

aws lambda remove-permission --function-name arn:aws:lambda:us-east-1:420279361566:function:updateContent-updateContent-4RACAC98G05Q --statement-id api-gateway-invoke


ARN: arn:aws:execute-api:us-east-1:420279361566:ktj2974nv7/*/POST/doctor
