# How to create EC2 with User Data using CDK Python pre-configured with Streamlit App file
This project showcases how to create an EC2 instance with CDK Python with the addtion of the `User Data` script. User Data script helps pre-install all the required updates and helps create a ready to consume platform to hit the ground running. 

In this example, Users sets up an EC2 with CDK that prepares to install and run streamlit app on EC2

**1. User deploys this CDK to create EC2. The EC2 is created with following configurations**
1.1. EC2 creation with appropriate Security groups, Pairing Keys
1.2. HTTP Outbound rules that allows Streamlit to host
1.3. Creates HTTP with port required for the Streamlit
1.4. Contains the `User Data` that installs the latest updates
1.5. `User Data` also copies a sample streamlit app in the path /home/ec2-user/streamlit-app. The file app.py contains the sample streamlit app that users can modify to suite her purpose  

**2. As a one time activity, User then installs Streamlit manually accessing the EC2. Here are the manual steps listed**
2.1. Access the EC2 with Online Navigate on AWS Console>EC2>Instances>Select `/home/ec2-user/streamlit-app`. Then click Connect for online access of the EC2
2.2. Install the streamlit type `pip3 install streamlit`

**3. Launch the Streamlit App for Temporary Testing**
3.1. Launch the streamlit app.py by typing following command `streamlit run /home/ec2-user/streamlit-app/app.py`
3.2. Copy paste the External URL generated in Web Browser to access the Streamlit App 

**4. Launch the Streamlit App for Permanent**
4.1. Launch the streamlit app.py by typing following command `nohup python3 -m streamlit run /home/ec2-user/streamlit-app/app.py`
4.2. Copy paste the External URL generated in Web Browser to access the Streamlit App

**5. For any enhancemnet in the streamlit app, the users can modify the the files app.py `home/ec2-user/streamlit-app/app.py`**



# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
