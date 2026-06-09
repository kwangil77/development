FROM docker.io/busybox
LABEL maintainer="Kwangil Ha <kwangil77@hotmail.com>"
ADD https://github.com/grafana/otel-profiling-java/releases/download/v2.0.5/pyroscope-otel-javaagent-extension.jar /extensions/pyroscope-otel-javaagent-extension.jar
RUN chmod -R go+r /extensions/pyroscope-otel-javaagent-extension.jar