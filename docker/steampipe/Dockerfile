FROM docker.io/library/debian:bookworm-slim
LABEL maintainer="Kwangil Ha <kwangil77@hotmail.com>"

ARG TARGETARCH

RUN apt update \
    && apt -y install curl \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --system --disabled-login --ingroup 0 --gecos "steampipe user" --shell /bin/false --uid 9193 --home /home/steampipe steampipe

RUN curl -sSL -o /tmp/steampipe.tar.gz https://github.com/turbot/steampipe/releases/download/v2.1.0/steampipe_linux_${TARGETARCH}.tar.gz \
    && tar xvzf /tmp/steampipe.tar.gz -C /tmp \
    && mv /tmp/steampipe /usr/local/bin/steampipe \
    && rm -rf /tmp/steampipe*

RUN curl -sSL -o /usr/local/bin/aws-iam-authenticator https://github.com/kubernetes-sigs/aws-iam-authenticator/releases/download/v0.7.4/aws-iam-authenticator_0.7.4_linux_${TARGETARCH} \
    && chmod +x /usr/local/bin/aws-iam-authenticator

USER steampipe:0

WORKDIR /workspace

ENV STEAMPIPE_UPDATE_CHECK=false
ENV STEAMPIPE_TELEMETRY=none

RUN steampipe service start \
    && steampipe service stop \
    && rm -f ./mod.sp

EXPOSE 9193

CMD [ "steampipe", "service", "start", "--foreground" ]
