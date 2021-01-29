#!/usr/bin/env bash
echo "Installing Pipeline Operators" 
oc get project $1

if [ $? -eq 1 ];then
  oc new-project $1
fi

oc project $1
helm install lab-operators-$1 --dry-run=false ./helm/lab-pipeline-tools/pipeline-operators/ --set namespace=$1
