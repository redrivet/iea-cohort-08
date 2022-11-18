import boto3

client = boto3.client('sdb', region_name="us-east-1")

response = client.create_domain(
    DomainName='ninja-turtles'
)
print(response)
