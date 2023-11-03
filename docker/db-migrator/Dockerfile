FROM harbor.example.io/docker.io/artifacthub/db-migrator
LABEL maintainer="Kwangil Ha <kwangil77@hotmail.com>"
USER root
RUN sed -ri 's/create extension tsm_system_rows/create extension if not exists tsm_system_rows/' schema/024_tsm_system_rows_extension.sql \
    && sed -ri 's/create extension pg_partman/create extension if not exists pg_partman/' schema/032_packages_views.sql \
    && sed -ri 's/drop extension pg_partman/-- drop extension pg_partman/' schema/034_partman_schema.sql \
    && sed -ri 's/create extension pg_partman/-- create extension pg_partman/' schema/034_partman_schema.sql \
    && sed -ri 's/create schema partman/-- create extension pg_partman/' schema/034_partman_schema.sql \
    && sed -ri 's/select partman.create_parent/-- select partman.create_parent/' schema/034_partman_schema.sql
USER 1000