#!/usr/bin/env bash
echo "Installing Openshift 4"
cd config/ocp-demo-cluster
rm -rf ./ocp-install
mkdir ocp-install
cp ./ocp-config/install-config.yaml ./ocp-install/
openshift-install create cluster --dir=./ocp-install
