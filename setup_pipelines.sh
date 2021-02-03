#!/usr/bin/env bash
if [[ -z "$MY_GIT_USERNAME" ]]; then
    echo "Must provide MY_GIT_USERNAME  base64 encyptyed the in environment" 1>&2
    exit 1
fi
if [[ -z "$MY_GIT_TOKEN" ]]; then
    echo "Must provide MY_GIT_TOKEN  base64 encyptyed the in environment" 1>&2
    exit 1
fi
OC_STATUS=$(oc whoami)
if [[ -z "$OC_STATUS" ]]; 
then
  echo "Must be logged into a Cluster"
  exit 1
fi

./config/cluster-config/install.sh cicd-tools
./config/pipeline-operators/install.sh cicd-tools
sleep 60s
echo "Installing Pipeline" 
oc project cicd-tools
helm install cicd-tools ./helm/lab-pipeline-tools/pipeline-tools/

echo "Configuring pipelines"
SONAR_ROUTE=$(oc get route sonarqube-insecure --no-headers=true | awk '{ print $2 }')
echo $SONAR_ROUTE

if [[ -z "$MY_GOOGLECHAT_TOKEN" ]]; then
helm template pipelines helm/argo-applications/ --set googlechat_secret=$MY_GOOGLECHAT_SECRET --set googlechat_channel=$MY_GOOGLECHAT_CHANNEL --set googlechat_token=$MY_GOOGLECHAT_TOKEN --set googlechat_key=$MY_GOOGLECHAT_KEY --set sonar_route=http://$SONAR_ROUTE  --set github_secret_username=$MY_GIT_USERNAME  --set github_secret_username=$MY_GIT_USERNAME  | oc apply -f-
else
helm template pipelines helm/argo-applications/ --set github_secret_username=$MY_GIT_USERNAME --set github_secret_token=$MY_GIT_TOKEN --set sonar_route=http://$SONAR_ROUTE | oc apply -f-
fi
