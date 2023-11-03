# Boundary

[Boundary](https://boundaryproject.io/) enables identity-based access management for dynamic infrastructure.

## Installing the Chart

Before you can install the chart you will need to add the `example` repo to [Helm](https://helm.sh/).

```shell
helm repo add example https://nexus.example.io/repository/helm-hosted
```

After you've installed the repo you can install the chart.

```shell
helm upgrade --install --namespace default --values ./my-values.yaml my-release example/boundary
```

## Configuration

The following table lists the configurable parameters of the _Boundary_ chart and their default values.

| Parameter                                 | Description                                                                                                                      | Default                             |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `nameOverride`                            | Override the name of the chart.                                                                                                  | `nil`                               |
| `fullnameOverride`                        | Override the fullname of the chart.                                                                                              | `nil`                               |
| `serviceAccount.create`                   | If `true`, create a new service account.                                                                                         | `true`                              |
| `serviceAccount.annotations`              | Annotations to add to the service account.                                                                                       | `{}`                                |
| `serviceAccount.name`                     | Service account to be used. If not set and `serviceAccount.create` is `true`, a name is generated using the _fullname_ template. | `nil`                               |
| `image.repository`                        | Image repository for the image.                                                                                                  | `hashicorp/boundary`                |
| `image.tag`                               | Image tag for the image.                                                                                                         | `{{ .Chart.AppVersion }}`           |
| `image.pullPolicy`                        | Image pull policy for the image.                                                                                                 | `IfNotPresent`                      |
| `image.pullSecrets`                       | Image pull secrets for the image.                                                                                                | `[]`                                |
| `controller.replicaCount`                 | Number of controller pods.                                                                                                       | `1`                                 |
| `controller.podAnnotations`               | Annotations to add to the controller pod.                                                                                        | `{}`                                |
| `controller.podLabels`                    | Labels to add to the controller pod.                                                                                             | `{}`                                |
| `controller.podSecurityContext`           | Security context for the controller pod.                                                                                         | `{}`                                |
| `controller.securityContext`              | Security context for the primary controller container.                                                                           | `{}`                                |
| `controller.priorityClassName`            | Priority class name to use for controller pod.                                                                                   | `""`                                |
| `controller.livenessProbe`                | The liveness probe for controller pods.                                                                                          | See _values.yaml_                   |
| `controller.readinessProbe`               | The readiness probe for controller pods.                                                                                         | See _values.yaml_                   |
| `controller.service.type`                 | Service type for controller.                                                                                                     | `ClusterIP`                         |
| `controller.service.annotations`          | Annotations to add to the controller service.                                                                                    | `{}`                                |
| `controller.service.port`                 | Service port for controller.                                                                                                     | `80`                                |
| `controller.ingress.enabled`              | If `true`, create an ingress object for controller.                                                                              | `false`                             |
| `controller.ingress.annotations`          | Ingress annotations for controller.                                                                                              | `{}`                                |
| `controller.ingress.ingressClassName`     | Ingress class to use for controller.                                                                                             | `""`                                |
| `controller.ingress.hosts`                | Ingress hosts for controller.                                                                                                    | `[]`                                |
| `controller.ingress.tls`                  | Ingress TLS configuration for controller                                                                                         | `[]`                                |
| `controller.resources`                    | Resource requests and limits for the primary controller container.                                                               | `{}`                                |
| `controller.nodeSelector`                 | Node labels for controller pod assignment.                                                                                       | `{}`                                |
| `controller.tolerations`                  | Toleration labels for controller pod assignment.                                                                                 | `[]`                                |
| `controller.affinity`                     | Affinity settings for controller pod assignment.                                                                                 | `{}`                                |
| `controller.env`                          | Environment variables for the _boundary_ and default init containers.                                                            | `[]`                                |
| `controller.config`                       | Config for all containers in the controller pod.                                                                                 | `{}`                                |
| `worker.podAnnotations`                   | Annotations to add to the worker pod.                                                                                            | `{}`                                |
| `worker.podLabels`                        | Labels to add to the worker pod.                                                                                                 | `{}`                                |
| `worker.podSecurityContext`               | Security context for the worker pod.                                                                                             | `{}`                                |
| `worker.securityContext`                  | Security context for the primary worker container.                                                                               | `{}`                                |
| `worker.priorityClassName`                | Priority class name to use for worker pod.                                                                                       | `""`                                |
| `worker.resources`                        | Resource requests and limits for the primary worker container.                                                                   | `{}`                                |
| `worker.nodeSelector`                     | Node labels for worker pod assignment.                                                                                           | `{}`                                |
| `worker.tolerations`                      | Toleration labels for worker pod assignment.                                                                                     | `[]`                                |
| `worker.affinity`                         | Affinity settings for worker pod assignment.                                                                                     | `{}`                                |
| `worker.config`                           | Config for all containers in the worker pod.                                                                                     | `{}`                                |