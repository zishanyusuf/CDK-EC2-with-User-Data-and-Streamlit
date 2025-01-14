from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    CfnOutput
)
from constructs import Construct

class CdkStreamlitEc2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Create the EC2, it contains the following steps
        #Step 1. Create VPC, pre-requiste to create the EC2
        vpc = ec2.Vpc(
            self,
            "StreamlitEc2Vpc", #Mandatory field
            max_azs=2, #Optional - Defines the max AZ
            subnet_configuration=[ #Optional - Defines the subnet configuration. by default it creates the Public and Private both and distribute the CIDER equally. But here we force just to create the public only
                ec2.SubnetConfiguration(
                    name="public-subnet-1",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                )
            ],
        )
        
        #Step 2. Create Security Group, pre-requiste to create the EC2
        sec_group = ec2.SecurityGroup(
            self, "StreamlitEc2SecurityGroup",
            vpc=vpc,
            allow_all_outbound=True,
        )
        
        #Add inbound rules in the Above Security group to allow HTTP, HTTPS traffic + Streamlit port traffic 
        #Step 2.1 Add inbound rule for HTTP (port 80)
        sec_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(80),
            description="Allow HTTP traffic"
        )
        #Step 2.2 Add inbound rule for HTTPS (port 443)
        sec_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(443),
            description="Allow HTTPS traffic"
        )
        #Step 2.3 Add inbound rule for Streamlit (port 8501)
        sec_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(8501),
            description="Allow Streamlit traffic"
        )
        #Step 2.4 Add inbound rule for SSH (port 22). This will help launch EC2 CLI on the web console
        sec_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(),
            connection=ec2.Port.tcp(22),
            description="Allow SSH traffic"
        )

        #Step 3. Create Key Pair, pre-requiste to create the EC2
        cfn_key_pair = ec2.CfnKeyPair(
            self, "StreamlitEc2KeyPair",
            key_name="streamlit-key-pair",
        )
                
        #Step 4. Finally create the EC2 in last steps
        instance = ec2.Instance(
            self,
            "StreamlitInstance",
            instance_type=ec2.InstanceType("t2.small"),
            machine_image=ec2.MachineImage.latest_amazon_linux(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            vpc=vpc,
            security_group=sec_group,
            associate_public_ip_address=True,
            key_name=cfn_key_pair.key_name
        )
        
        #Add User Data to the EC2
        with open("./user_data.sh", "r") as file:
            user_data_script = file.read()
        instance.add_user_data(user_data_script)
        
        # Output Instance ID
        CfnOutput(self, "InstanceId", value=instance.instance_id)
