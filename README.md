# ocp-labs-manager

subscription-manager register
    7  subscription-manager -u mlacours@redhat.com
    8  sudo subscription-manager register
    9  sudo yum install git
   10  ls
   11  git clone https://github.com/redhat-mal/ocp-labs-manager.git
   12  ls
   13  rm -rf attlabs/
   14  wget https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.6/openshift-client-linux.tar.gz
   15  sudo yum install wget -y
   16  wget https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.6/openshift-client-linux.tar.gz
   17  wget https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.6/openshift-install-linux.tar.gz
   18  ls -lrt
   19  tar -xvf ./openshift-client-linux.tar.gz 
   20  sudo mv oc /usr/local/bin
   21  sudo mv kubectl /usr/local/bin
   22  ls
   23  oc version
   24  tar -xvf ./openshift-install-linux.tar.gz 
   25  ls
   26  pwd
   27  sudo mv openshift-install /usr/local/bin
   28  cd ocp-labs-manager/
   29  ls
   30  openshift-install
   31  openshift-install create config
   32  openshift-install create install-config
   33  ls
   34  vi install-config.yaml 
   35  rm install-config.yaml 
   36  ls
   37  ./config/ocp-demo-cluster/install.sh ./config/ocp-demo-cluster/
