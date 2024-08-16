FROM docker.io/library/debian:bookworm-slim
LABEL maintainer="Kwangil Ha <kwangil77@hotmail.com>"

RUN apt update \
    && apt -y install curl \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --system --disabled-login --ingroup 0 --gecos "steampipe user" --shell /bin/false --uid 9193 --home /home/steampipe steampipe

RUN curl -sSL -o /tmp/steampipe.tar.gz https://github.com/turbot/steampipe/releases/download/v0.23.4/steampipe_linux_amd64.tar.gz \
    && tar xvzf /tmp/steampipe.tar.gz -C /tmp \
    && mv /tmp/steampipe /usr/local/bin/steampipe \
    && rm -rf /tmp/steampipe*

USER steampipe:0

WORKDIR /workspace

ENV STEAMPIPE_UPDATE_CHECK=false
ENV STEAMPIPE_TELEMETRY=none

RUN steampipe service start \
    && steampipe service stop \
    && rm -f ./mod.sp

EXPOSE 9193

CMD [ "steampipe", "service", "start", "--foreground" ]
