import boto3

# Get a SimpleDB client object
client = boto3.client('sdb', region_name="us-east-1")

# Create a Domain
response = client.create_domain(
    DomainName='ninja-turtles'
)

# Add an item and data attributes
response = client.put_attributes(
    DomainName='ninja-turtles',
    ItemName='Donnatello',
    Attributes=[
        {
            'Name': 'nickname',
            'Value': 'Donny',
        },
    ],
)

# Retrieve attributes from an item
response = client.get_attributes(
    DomainName='ninja-turtles',
    ItemName='Donnatello',
    AttributeNames=[
        'nickname'
    ],
)

print(response)

# Update Attributes on an item
response = client.put_attributes(
    DomainName='ninja-turtles',
    ItemName='Donatello',
    Attributes=[
        {
            'Name': 'nickname',
            'Value': 'Donny',
        },
        {
            'Name': 'nickname',
            'Value': 'Don',
        },
    ],
)

# Show the update results
response = client.get_attributes(
    DomainName='ninja-turtles',
    ItemName='Donnatello',
    AttributeNames=[
        'nickname'
    ],
)

print(response)

# Remove the domain to clean up
response = client.get_attributes(
    DomainName='ninja-turtles',
    ItemName='Donnatello',
    AttributeNames=[
        'nickname'
    ],
)

print(response)
