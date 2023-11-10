FROM docker.io/alpine/k8s:1.27.4
LABEL maintainer="Kwangil Ha <kwangil77@hotmail.com>"
RUN curl -sSL -o /usr/local/bin/argocd-vault-plugin https://github.com/argoproj-labs/argocd-vault-plugin/releases/download/v1.16.1/argocd-vault-plugin_1.16.1_linux_amd64 \
    && chmod +x /usr/local/bin/argocd-vault-plugin