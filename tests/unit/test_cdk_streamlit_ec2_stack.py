import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_streamlit_ec2.cdk_streamlit_ec2_stack import CdkStreamlitEc2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_streamlit_ec2/cdk_streamlit_ec2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkStreamlitEc2Stack(app, "cdk-streamlit-ec2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
