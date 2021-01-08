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
cat > ~/.aws/credentials << EOF
[default]
aws_access_key_id = <your key ID>
aws_secret_access_key = <your key>
EOF
```

#### Configure Required tools

```
sudo subscription-manager register
sudo yum install git -y
sudo yum install wget -y
```

Install Helm3
```
sudo dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo yum install snapd

## Wait for a minute
sudo snap install helm3
```

Clone the labs manager repo
'''
git clone https://github.com/redhat-mal/ocp-labs-manager.git
'''

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

```
cd ocp-labs-manager/
./config/ocp-demo-cluster/install.sh ./config/ocp-demo-cluster/
```

### Run cluster config after install to setiup htpasswd
```
 ./config/cluster-config/install.sh cicd-tools
 ```

### Install Pipeeline and ArgoCD operator
```
./config/pipeline-operators/install.sh cicd-tools ./config/pipeline-operators/
```

### Install ArgoCd and SonarQube

```
cd ocp-labs-manager/helm/lab-pipeline-tools/pipeline-tools/
oc login https://api.att-demo.ocp-labs.rhtelco.io:6443
oc project cicd-tools
helm install cicd-tools .
```

### Configure Demo Pipelines in ArgoCD
```
cd helm/argo-applications/
helm template pipelines . | oc apply -f-
```



