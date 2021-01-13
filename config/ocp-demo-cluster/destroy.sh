#!/usr/bin/env bash
cd config/ocp-demo-cluster
openshift-install destroy cluster --dir=./ocp-install
