# Import modules
import boto3

# Function creats a CloudFormation stack
def create_stack():

    # Create the stack
    cloudformation.create_stack(
        StackName='simian-targets',
        TemplateURL='https://s3-eu-west-1.amazonaws.com/dave-general/simian-targets.yaml',
        Parameters=[
            {
                'ParameterKey': 'ImageId',
                'ParameterValue': 'ami-7abd0209'
            },
            {
                'ParameterKey': 'InstanceType',
                'ParameterValue': 't2.micro'
            },
            {
                'ParameterKey': 'SubnetIds',
                'ParameterValue': 'subnet-5d502c39,subnet-9f117ae9,subnet-1496284c'
            }
        ],
        Tags=[
            {
                'Key': 'Name',
                'Value': 'simian-targets'
            },
            {
                'Key': 'System',
                'Value': 'simian-army'
            }
        ]
    )

# Function creats a CloudFormation stack
def update_stack():

    # Create the stack
    cloudformation.update_stack(
        StackName='simian-targets',
        TemplateURL='https://s3-eu-west-1.amazonaws.com/dave-general/simian-targets.yaml',
        Parameters=[
            {
                'ParameterKey': 'ImageId',
                'ParameterValue': 'ami-7abd0209'
            },
            {
                'ParameterKey': 'InstanceType',
                'ParameterValue': 't2.micro'
            },
            {
                'ParameterKey': 'SubnetIds',
                'ParameterValue': 'subnet-5d502c39,subnet-9f117ae9,subnet-1496284c'
            }
        ],
        Tags=[
            {
                'Key': 'Name',
                'Value': 'simian-targets'
            },
            {
                'Key': 'System',
                'Value': 'simian-army'
            }
        ]
    )

# Connect to cloudformation and S3 with the default profile
cloudformation = boto3.client('cloudformation')
s3 = boto3.client('s3')

# Upload latest template file to S3
s3.upload_file('simian-targets.yaml', 'dave-general', 'simian-targets.yaml')

# Try to describe the stack, which will fail if it does not exist
try:
    status = cloudformation.describe_stacks(StackName='simian-targets')

    # It exists, so update it
    update_stack()

except Exception as e:

    # It doesn't exist, so create it
    create_stack()
