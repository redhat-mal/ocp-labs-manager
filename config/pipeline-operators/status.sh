#!/usr/bin/env bash
export KUBECONFIG=./config/ocp-demo-cluster/ocp-install/auth/kubeconfig
oc login -u system:admin >> /dev/null

###echo "GETTGING STATUS FOR $1"

helm status --skip-headers=true --output=json lab-operators-$1 >> /dev/null
if [ $? -eq 0 ];then
  echo "installed"
  exit 0
else
  echo "deleted"
  exit 0
fi

