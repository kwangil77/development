FROM quay.io/ansible/awx-ee
LABEL maintainer="Kwangil Ha <kwangil77@hotmail.com>"
USER root
COPY id_rsa /root/.ssh/id_rsa
COPY id_rsa.pub /root/.ssh/id_rsa.pub
RUN dnf install -y unzip \
    && ln -sf /usr/bin/python3 /usr/libexec/platform-python \
    && chmod 700 /root/.ssh \
    && chmod 644 /root/.ssh/id_rsa.pub \
    && chmod 600 /root/.ssh/id_rsa \
    && ansible-galaxy collection install community.general --collections-path /usr/share/ansible/collections \
    && ansible-galaxy collection install community.docker --collections-path /usr/share/ansible/collections \
    && ansible-galaxy collection install community.aws --collections-path /usr/share/ansible/collections \
    && pip install passlib \
    && curl -sSL -o /tmp/terraform.zip https://releases.hashicorp.com/terraform/1.11.4/terraform_1.11.4_linux_amd64.zip \
    && unzip /tmp/terraform.zip -d /usr/local/bin \
    && curl -sSL -o /tmp/helm.tar.gz https://get.helm.sh/helm-v3.17.3-linux-amd64.tar.gz \
    && tar xzvf /tmp/helm.tar.gz -C /tmp \
    && mv /tmp/linux-amd64/helm /usr/local/bin \
    && curl -sSL -o /usr/local/bin/aws-iam-authenticator https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v0.7.2/aws-iam-authenticator_0.7.2_linux_amd64 \
    && chmod +x /usr/local/bin/aws-iam-authenticator \
    && rm -rf /tmp/*
USER 1000