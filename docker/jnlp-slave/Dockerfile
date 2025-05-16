FROM docker.io/jenkins/jnlp-slave:latest-jdk11
LABEL maintainer="Kwangil Ha <kwangil77@hotmail.com>"
USER root
RUN apt update \
    && apt -y install locales sudo zip jq libicu63 \
    && localedef -c -i en_US -f UTF-8 en_US.UTF-8 \
    && curl -sSL -o /tmp/docker.tgz https://download.docker.com/linux/static/stable/x86_64/docker-28.1.1.tgz \
    && tar xvzf /tmp/docker.tgz -C /tmp \
    && mv /tmp/docker/docker /usr/local/bin/docker \
    && rm -rf /tmp/docker* \
    && curl -sSL -o /tmp/awscli.zip https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip \
    && unzip /tmp/awscli.zip -d /tmp \
    && /tmp/aws/install \
    && rm -rf /tmp/aws* \
    && curl -sSL -o /tmp/samcli.zip https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip \
    && unzip /tmp/samcli.zip -d /tmp/sam \
    && /tmp/sam/install \
    && rm -rf /tmp/sam* \
    && curl -sSL -o /usr/local/bin/cyclonedx https://github.com/CycloneDX/cyclonedx-cli/releases/latest/download/cyclonedx-linux-x64 \
    && chmod +x /usr/local/bin/cyclonedx \
    && curl -sSL -o /usr/local/bin/aws-iam-authenticator https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v0.7.2/aws-iam-authenticator_0.7.2_linux_amd64 \
    && chmod +x /usr/local/bin/aws-iam-authenticator \
    && curl -sSL -o /usr/local/bin/kubectl https://dl.k8s.io/release/v1.33.0/bin/linux/amd64/kubectl \
    && chmod +x /usr/local/bin/kubectl \
    && echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers \
    && rm -rf /var/lib/apt/lists/*
USER jenkins