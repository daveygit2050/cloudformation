# Import modules
import boto3

# Function creats a CloudFormation stack
def create_stack():

    # Create the stack
    cloudformation.create_stack(
        StackName='chef-bamboo',
        TemplateURL='https://s3-eu-west-1.amazonaws.com/dave-general/chef-bamboo.yaml',
        Parameters=[
            {
                'ParameterKey': 'FQDN',
                'ParameterValue': 'bamboo.randall-it.uk'
            },
            {
                'ParameterKey': 'HostedZoneId',
                'ParameterValue': 'Z35V1WYGMHE3VE'
            },
            {
                'ParameterKey': 'ImageId',
                'ParameterValue': 'ami-7abd0209'
            },
            {
                'ParameterKey': 'InstanceType',
                'ParameterValue': 't2.micro'
            },
            {
                'ParameterKey': 'KeyName',
                'ParameterValue': 'dave'
            },
            {
                'ParameterKey': 'PublicIpAddress',
                'ParameterValue': '79.66.193.146'
            },
            {
                'ParameterKey': 'SubnetIds',
                'ParameterValue': 'subnet-5d502c39,subnet-9f117ae9,subnet-1496284c'
            },
            {
                'ParameterKey': 'VpcId',
                'ParameterValue': 'vpc-46891722'
            }
        ],
        Capabilities=['CAPABILITY_IAM'],
        Tags=[
            {
                'Key': 'Name',
                'Value': 'chef-bamboo'
            },
            {
                'Key': 'System',
                'Value': 'bamboo'
            }
        ]
    )

# Function creats a CloudFormation stack
def update_stack():

    # Create the stack
    cloudformation.update_stack(
        StackName='chef-bamboo',
        TemplateURL='https://s3-eu-west-1.amazonaws.com/dave-general/chef-bamboo.yaml',
        Parameters=[
            {
                'ParameterKey': 'FQDN',
                'ParameterValue': 'bamboo.randall-it.uk'
            },
            {
                'ParameterKey': 'HostedZoneId',
                'ParameterValue': 'Z35V1WYGMHE3VE'
            },
            {
                'ParameterKey': 'ImageId',
                'ParameterValue': 'ami-7abd0209'
            },
            {
                'ParameterKey': 'InstanceType',
                'ParameterValue': 't2.micro'
            },
            {
                'ParameterKey': 'KeyName',
                'ParameterValue': 'dave'
            },
            {
                'ParameterKey': 'PublicIpAddress',
                'ParameterValue': '79.66.193.146'
            },
            {
                'ParameterKey': 'SubnetIds',
                'ParameterValue': 'subnet-5d502c39,subnet-9f117ae9,subnet-1496284c'
            },
            {
                'ParameterKey': 'VpcId',
                'ParameterValue': 'vpc-46891722'
            }
        ],
        Capabilities=['CAPABILITY_IAM'],
        Tags=[
            {
                'Key': 'Name',
                'Value': 'chef-bamboo'
            },
            {
                'Key': 'System',
                'Value': 'bamboo'
            }
        ]
    )

# Connect to cloudformation and S3 with the default profile
cloudformation = boto3.client('cloudformation')
s3 = boto3.client('s3')

# Upload latest template file to S3
s3.upload_file('chef-bamboo.yaml', 'dave-general', 'chef-bamboo.yaml')

# Try to describe the stack, which will fail if it does not exist
try:
    status = cloudformation.describe_stacks(StackName='chef-bamboo')

    # It exists, so update it
    update_stack()

except Exception as e:

    # It doesn't exist, so create it
    create_stack()
