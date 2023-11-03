# AWS ECR Proxy

[AWS ECR Proxy](https://github.com/GfK-NORM/aws-ecr-proxy) is a very simple nginx push/pull proxy that forwards requests to AWS ECR.

## Installing the Chart

Before you can install the chart you will need to add the `example` repo to [Helm](https://helm.sh/).

```shell
helm repo add example https://nexus.example.io/repository/helm-hosted
```

After you've installed the repo you can install the chart.

```shell
helm upgrade --install --namespace default --values ./my-values.yaml my-release example/aws-ecr-proxy
```

## Configuration

The following table lists the configurable parameters of the _AWS ECR Proxy_ chart and their default values.

| Parameter                          | Description                                                                                                                      | Default                             |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `image.repository`                 | Image repository.                                                                                                                | `gfknorm/aws-ecr-proxy`             |
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
| `service.port`                     | Service port.                                                                                                                    | `9000`                              |
| `ingress.enabled`                  | If `true`, create an ingress object.                                                                                             | `false`                             |
| `ingress.annotations`              | Ingress annotations.                                                                                                             | `{}`                                |
| `ingress.ingressClassName`         | Ingress class to use.                                                                                                            | `""`                                |
| `ingress.hosts`                    | Ingress hosts.                                                                                                                   | `[]`                                |
| `ingress.tls`                      | Ingress TLS configuration                                                                                                        | `[]`                                |
| `resources`                        | Resource requests and limits for the primary container.                                                                          | `{}`                                |
| `replicaCount`                     | Number of replicas to run.                                                                                                       | `1`                                 |
| `nodeSelector`                     | Node labels for pod assignment.                                                                                                  | `{}`                                |
| `tolerations`                      | Toleration labels for pod assignment.                                                                                            | `[]`                                |
| `affinity`                         | Affinity settings for pod assignment.                                                                                            | `{}`                                |
| `env`                              | Environment variables for the _aws-ecr-proxy_ and default init containers.                                                       | `[]`                                |
| `config`                           | Config for all containers in the pod.                                                                                            | See _values.yaml_                   |