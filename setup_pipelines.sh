#!/usr/bin/env bash
./config/cluster-config/install.sh cicd-tools
./config/pipeline-operators/install.sh cicd-tools
sleep 30s
echo "Installing Pipeline" 
export KUBECONFIG=./config/ocp-demo-cluster/ocp-install/auth/kubeconfig
oc login -u system:admin
oc project cicd-tools
helm install cicd-tools ./helm/lab-pipeline-tools/pipeline-tools/

echo "Configuring pipelines"
SONAR_ROUTE=$(oc get route sonarqube-insecure --no-headers=true | awk '{ print $2 }')
echo $SONAR_ROUTE

helm template pipelines helm/argo-applications/ --set sonar_route=http://$SONAR_ROUTE | oc apply -f-
