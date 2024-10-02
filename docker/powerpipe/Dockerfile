FROM docker.io/library/debian:bookworm-slim
LABEL maintainer="Kwangil Ha <kwangil77@hotmail.com>"

ARG TARGETARCH

RUN apt update \
    && apt -y install curl \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --system --disabled-login --ingroup 0 --gecos "powerpipe user" --shell /bin/false --uid 9033 --home /home/powerpipe powerpipe

RUN curl -sSL -o /tmp/powerpipe.tar.gz https://github.com/turbot/powerpipe/releases/download/v0.4.4/powerpipe.linux.${TARGETARCH}.tar.gz \
    && tar xvzf /tmp/powerpipe.tar.gz -C /tmp \
    && mv /tmp/powerpipe /usr/local/bin/powerpipe \
    && rm -rf /tmp/powerpipe*

USER powerpipe:0

WORKDIR /workspace

ENV POWERPIPE_UPDATE_CHECK=false
ENV POWERPIPE_TELEMETRY=none

EXPOSE 9033

CMD [ "powerpipe", "server" ]
