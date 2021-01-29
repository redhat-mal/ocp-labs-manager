FROM quay.io/bitnami/git:latest

ENV OCP_VER=4.6.9

RUN curl -LO https://github.com/github/hub/releases/download/v2.14.2/hub-linux-amd64-2.14.2.tgz && \
    tar -xvf hub-linux-amd64-2.14.2.tgz && \
    ./hub-linux-amd64-2.14.2/install 

RUN curl -LO https://mirror.openshift.com/pub/openshift-v4/clients/ocp/$OCP_VER/openshift-client-linux-$OCP_VER.tar.gz && \
    tar -xvf openshift-client-linux-$OCP_VER.tar.gz && \
    mv oc /usr/local/bin




