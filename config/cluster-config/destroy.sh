#!/usr/bin/env bash
echo "Installing Cluster Config" 
export KUBECONFIG=./config/ocp-demo-cluster/ocp-install/auth/kubeconfig
oc login -u system:admin

if [ $? -eq 1 ];then
  exit 2
fi

helm template cluster-config ./helm/cluster-configuration/ --set namespace=$1 --set remove_config=true  | oc apply -f-

oc delete clusterrolebinding att-lab-user-roles -n $1
oc delete secret htpasswd-demo -n openshift-config
cat > $2/install-status << EOF2
deleted
EOF2
oc delete project $1
