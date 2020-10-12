#!/usr/bin/env bash
export KUBECONFIG=./config/ocp-demo-cluster/ocp-install/auth/kubeconfig
oc login -u system:admin >> /dev/null

###echo "GETTGING STATUS FOR $1"

cat $2/install-status
exit 0

