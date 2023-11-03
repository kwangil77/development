# SourceGraph

[SourceGraph](https://about.sourcegraph.com/) is a fast, fully-featured code search and navigation engine.

## Installing the Chart

Before you can install the chart you will need to add the `example` repo to [Helm](https://helm.sh/).

```shell
helm repo add example https://nexus.example.io/repository/helm-hosted
```

After you've installed the repo you can install the chart.

```shell
helm upgrade --install --namespace default --values ./my-values.yaml my-release example/sourcegraph
```

## Configuration

The following table lists the configurable parameters of the _SourceGraph_ chart and their default values.

| Parameter                          | Description                                                                                                                      | Default                             |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `image.repository`                 | Image repository.                                                                                                                | `sourcegraph/server`                |
| `image.tag`                        | Image tag.                                                                                                                       | `{{ .Chart.AppVersion }}`           |
| `image.pullPolicy`                 | Image pull policy.                                                                                                               | `IfNotPresent`                      |
| `image.pullSecrets`                | Image pull secrets.                                                                                                              | `[]`                                |
| `nameOverride`                     | Override the name of the chart.                                                                                                  | `nil`                               |
| `fullnameOverride`                 | Override the fullname of the chart.                                                                                              | `nil`                               |
| `serviceAccount.create`            | If `true`, create a new service account.                                                                                         | `true`                              |
| `serviceAccount.annotations`       | Annotations to add to the service account.                                                                                       | `{}`                                |
| `serviceAccount.name`              | Service account to be used. If not set and `serviceAccount.create` is `true`, a name is generated using the _fullname_ template. | `nil`                               |
| `podAnnotations`                   | Annotations to add to the pod.                                                                                                   | `{}`                                |
| `podLabels`                        | Labels to add to the pod.                                                                                                        | `{}`                                |
| `podSecurityContext`               | Security context for the pod.                                                                                                    | `{}`                                |
| `securityContext`                  | Security context for the primary container.                                                                                      | `{}`                                |
| `priorityClassName`                | Priority class name to use.                                                                                                      | `""`                                |
| `livenessProbe`                    | The liveness probe.                                                                                                              | See _values.yaml_                   |
| `readinessProbe`                   | The readiness probe.                                                                                                             | See _values.yaml_                   |
| `service.type`                     | Service type.                                                                                                                    | `ClusterIP`                         |
| `service.annotations`              | Annotations to add to the service.                                                                                               | `{}`                                |
| `service.port`                     | Service port.                                                                                                                    | `7080`                              |
| `ingress.enabled`                  | If `true`, create an ingress object.                                                                                             | `false`                             |
| `ingress.annotations`              | Ingress annotations.                                                                                                             | `{}`                                |
| `ingress.ingressClassName`         | Ingress class to use.                                                                                                            | `""`                                |
| `ingress.hosts`                    | Ingress hosts.                                                                                                                   | `[]`                                |
| `ingress.tls`                      | Ingress TLS configuration                                                                                                        | `[]`                                |
| `persistence.enabled`              | If `true`, create a PVC.                                                                                                         | `false`                             |
| `persistence.annotations`          | Annotations to add to the PVC.                                                                                                   | `{}`                                |
| `persistence.existingClaim`        | Use an existing PVC to persist data.                                                                                             | `nil`                               |
| `persistence.accessMode`           | Persistence access mode.                                                                                                         | `ReadWriteOnce`                     |
| `persistence.storageClass`         | PVC storage class (use `-` for default).                                                                                         | `standard`                          |
| `persistence.size`                 | Size of PVC to create.                                                                                                           | `8Gi`                               |
| `resources`                        | Resource requests and limits for the primary container.                                                                          | `{}`                                |
| `nodeSelector`                     | Node labels for pod assignment.                                                                                                  | `{}`                                |
| `tolerations`                      | Toleration labels for pod assignment.                                                                                            | `[]`                                |
| `affinity`                         | Affinity settings for pod assignment.                                                                                            | `{}`                                |
| `env`                              | Environment variables for the _sourcegraph_ and default init containers.                                                         | `[]`                                |
| `psql.host`                        | External _PostgreSQL_ host to use (if this is set the additional `psql` values need to be set)                                   | `nil`                               |
| `psql.port`                        | External _PostgreSQL_ port                                                                                                       | `nil`                               |
| `psql.database`                    | External _PostgreSQL_ database                                                                                                   | `nil`                               |
| `psql.username`                    | External _PostgreSQL_ username                                                                                                   | `nil`                               |
| `psql.password.secret`             | Name of the secret containing the external _PostgreSQL_ password                                                                 | `nil`                               |
| `psql.password.key`                | Key on the secret containing the external _PostgreSQL_ password                                                                  | `nil`                               |