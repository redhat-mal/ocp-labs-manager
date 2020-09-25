#!/usr/bin/env bash
echo "Installing Pipeline Operators" 
export KUBECONFIG=./config/ocp-demo-cluster/ocp-install/auth/kubeconfig
oc login -u system:admin

oc get project $1

if [ $? -eq 1 ];then
  exit 2
fi

oc project $1
helm uninstall lab-operators-$1
