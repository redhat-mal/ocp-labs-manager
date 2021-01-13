#!/usr/bin/env bash
echo "Applying Cluster Config" 
export KUBECONFIG=./config/ocp-demo-cluster/ocp-install/auth/kubeconfig
oc login -u system:admin
oc get project $1

if [ $? -eq 1 ];then
  oc new-project $1
fi

helm template cluster-config ./helm/cluster-configuration/ --set namespace=$1 | oc apply -f-

