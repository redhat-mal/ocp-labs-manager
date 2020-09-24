echo "Destroying Openshift 4"
cat > ./install-status << EOF
destroying
EOF
openshift-install destroy cluster --dir=./ocp-install
cat > ./install-status << EOF2
deleted
EOF2
