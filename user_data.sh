#! /bin/bash -x
sudo yum update
sudo yum upgrade -y
sudo yum install python3-pip -y
#Install the Git packages
sudo yum install git -y
#Clone the Git page containing the streamlit app
sudo mkdir -p /home/ec2-user/streamlit-app
cd /home/ec2-user/streamlit-app
sudo git clone https://github.com/zishanyusuf/Sample-Streamlit-App /home/ec2-user/streamlit-app
#pip install -r /home/ec2-user/streamlit-app/requirements.txt
python3 -m pip install -r /home/ec2-user/streamlit-app/requirements.txt
##Print the "User data script executed" into a log file (named user-data.log) within a path /var/log
echo 'User data script executed' > /var/log/user-data.log
