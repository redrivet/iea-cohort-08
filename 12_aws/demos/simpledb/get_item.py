import boto3

client = boto3.client('sdb', region_name="us-east-1")

response = client.get_attributes(
    DomainName='ninja-turtles',
    ItemName='Donatello',
    AttributeNames=[
        'nickname'
    ],
)

print(response)


