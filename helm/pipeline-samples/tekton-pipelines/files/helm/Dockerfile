FROM quay.io/bitnami/git:latest

ENV OCP_VER=4.6.9

RUN curl -LO https://mirror.openshift.com/pub/openshift-v4/clients/ocp/$OCP_VER/openshift-client-linux-$OCP_VER.tar.gz && \
    tar -xvf openshift-client-linux-$OCP_VER.tar.gz && \
    mv oc /usr/local/bin && \
    curl -L https://mirror.openshift.com/pub/openshift-v4/clients/helm/latest/helm-linux-amd64 -o /usr/local/bin/helm && \
    chmod +x /usr/local/bin/helm

ENTRYPOINT ["helm"]
CMD ["help"]




