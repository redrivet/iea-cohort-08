import boto3

client = boto3.client('sdb', region_name="us-east-1")

response = client.put_attributes(
    DomainName='ninja-turtles',
    ItemName='Leonardo',
    Attributes=[
        {
            'Name': 'nickname',
            'Value': 'Leo',
        },
    ],
)


