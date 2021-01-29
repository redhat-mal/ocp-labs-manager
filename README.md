# ocp-labs-manager


## Setup an AWS instanct to install OCP and Pipeline Demo

### Configure an AWS Instance in the Desired Region and Create AWS Keys 

1. Launch a "Red Hat Enterprise Linux 8" instance with size of t2.medium or larger.  
- add tags to ensure it is retained: 
    Contact	<email address>
    AlwaysUp	True
    DeleteBy	Never
    Name	< worker instance >

2. Create a AWS Key for your User

Use the AWW console IAM service and navigate to your user account and use the "Security Credentials" tab to create access keys.  Save the keys for later use.

3. Create a SSH key for the instance

When launching the instance either use an existing ssh key set or create a new key and download the public key.


### Conifigure the AWS instance to allow installs

1. ssh to the instance 

```
 ~/.ssh/<your key>  ec2-user@<your instance public dns>
```

2. Setup AWS Credentials

```
mkdir ~/.aws

cat > ~/.aws/credentials << EOF
[default]
aws_access_key_id = <your key ID>
aws_secret_access_key = <your key>
EOF
```

#### Configure Required tools (One Time)

```
sudo subscription-manager register
sudo yum install git -y
sudo yum install wget -y
```

Install Helm3
```
sudo curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-amd64 -o /usr/local/bin/helm
sudo chmod +x /usr/local/bin/helm
helm version
```
Download and configure openshift installer with desired version
```
wget https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.6/openshift-client-linux.tar.gz
wget https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.6/openshift-install-linux.tar.gz
tar -xvf ./openshift-client-linux.tar.gz 
sudo mv oc /usr/local/bin
sudo mv kubectl /usr/local/bin
tar -xvf ./openshift-install-linux.tar.gz 
sudo mv openshift-install /usr/local/bin
```

### Install OCP Cluster 

Clone the labs manager repo

```
git clone https://github.com/redhat-mal/ocp-labs-manager.git
```


Modify install-config.yaml under the path ocp-labs-manager/config/ocp-demo-cluster/ocp-config.
- Modify the name of the cluster on line 29
- 

```
cd ocp-labs-manager/
./config/ocp-demo-cluster/install.sh 
```

### Configure Github token for Pipelines to create pull request. (One Time)

Go to Github and navigate to settins -> Developer Settings
Navigate to "Personal Access Tokens"

Select "Generate new token"

Enable the Repo access the select "Generate"
Copy the value of the token

Run the following command and copy the output
```
export MY_GIT_TOKEN=$(echo "your token" | base64 --wrap=0)
export MY_GIT_USERNAME=$(echo "your username" | base64 --wrap=0)

```

### Run pipeline setup script to configure cluster auth and setup pipeline tools
```
 ./setup_pipelines.sh
 ```

### Configure Sample Spring App Pipeline (One Time)

Fork the spirng app repo to your account: https://github.com/redhat-mal/spring-rest-service.git


```
git clone https://github.com/<your account>/spring-rest-service.git
cd spring-rest-service
git fetch

# Modify repo for staging deployment
git checkout stage
vim .openshift/spring-boot-demo.yaml
# Modify line 36 to point to your github repo  and commit and push
git add .openshift/spring-boot-demo.yaml
git commit -m "fix repo"
git push origin stage:stage

# Modify repo for qa deployment
git checkout qa
vim .openshift/spring-boot-demo.yaml
# Modify line 24 to point to your github repo  and commit and push
git add .openshift/spring-boot-demo.yaml
git commit -m "fix repo"
git push origin qa:qa


# Configure Argo Apps
 ./setup_pipelines.sh
 ```

### Configure Webhook in Github using tekton event handler (One Time)

```
oc get route -n att-pipelines
```

Go to the github repo and select settings/webhooks
Create a new webhook with key of "ATT_DEMO_KEY" and the url of route.
Content type: application/json

![Github Webhook](github_wh.png)


### Modify app to initiate the build and deploy pipeline


```
# Deploy Argo App for Staging
git checkout main

# Modify the pom.xml and change version 
git add pom.xml
git commit -m "some message"
git push

```

### Merge Pull request in the spring app to promote to QA

Naviagate to the pull request tab for the spring-rest-service project
Merge the open pull request


## To Destory the Cluster

```
cd ocp-labs-manager/
./config/ocp-demo-cluster/destory.sh 
```


