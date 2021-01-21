#!/usr/bin/env bash
echo "Installing Openshift 4"
if [[ -z "$PULL_SECRET" ]]; then
    echo "Must provide PULL_SECRET in environment" 1>&2
    exit 1
fi
cd config/ocp-demo-cluster
rm -rf ./ocp-install
mkdir ocp-install
cp ./ocp-config/install-config.yaml ./ocp-install/
echo "add pull secret"
echo "pullSecret: $PULL_SECRET" >> ./ocp-install/install-config.yaml
#openshift-install create cluster --dir=./ocp-install
