#!/usr/bin/env bash
echo "Installing Openshift 4"
cd $1
rm -rf ./ocp-install
mkdir ocp-install
cp ./ocp-config/install-config.yaml ./ocp-install/
cat > ./install-status << EOF
installing
EOF
openshift-install create cluster --dir=./ocp-install
cat > ./install-status << EOF2
installed
EOF2
