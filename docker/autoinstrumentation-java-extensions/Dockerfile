FROM docker.io/busybox
LABEL maintainer="Kwangil Ha <kwangil77@hotmail.com>"
ADD https://github.com/grafana/otel-profiling-java/releases/download/v1.1.0/pyroscope-otel.jar /extensions/pyroscope-otel.jar
RUN chmod -R go+r /extensions/pyroscope-otel.jar