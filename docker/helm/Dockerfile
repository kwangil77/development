FROM docker.io/alpine/helm
LABEL maintainer="Kwangil Ha <kwangil77@hotmail.com>"
RUN curl -sSL -o /tmp/kustomize.tar.gz https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize%2Fv5.3.0/kustomize_v5.3.0_linux_amd64.tar.gz \
    && tar xvzf /tmp/kustomize.tar.gz -C /tmp \
    && mv /tmp/kustomize /usr/local/bin/kustomize \
    && rm -rf /tmp/kustomize* \
    && curl -sSL -o /usr/local/bin/argocd-vault-plugin https://github.com/argoproj-labs/argocd-vault-plugin/releases/download/v1.17.0/argocd-vault-plugin_1.17.0_linux_amd64 \
    && chmod +x /usr/local/bin/argocd-vault-plugin