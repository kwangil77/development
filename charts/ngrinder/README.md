# nGrinder

[nGrinder](http://naver.github.io/ngrinder/) is enterprise level performance testing solution based on the grinder.

## Installing the Chart

Before you can install the chart you will need to add the `example` repo to [Helm](https://helm.sh/).

```shell
helm repo add example https://nexus.example.io/repository/helm-hosted
```

After you've installed the repo you can install the chart.

```shell
helm upgrade --install --namespace default --values ./my-values.yaml my-release example/ngrinder
```

## Configuration

The following table lists the configurable parameters of the _nGrinder_ chart and their default values.

| Parameter                                 | Description                                                                                                                      | Default                             |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| `nameOverride`                            | Override the name of the chart.                                                                                                  | `nil`                               |
| `fullnameOverride`                        | Override the fullname of the chart.                                                                                              | `nil`                               |
| `serviceAccount.create`                   | If `true`, create a new service account.                                                                                         | `true`                              |
| `serviceAccount.annotations`              | Annotations to add to the service account.                                                                                       | `{}`                                |
| `serviceAccount.name`                     | Service account to be used. If not set and `serviceAccount.create` is `true`, a name is generated using the _fullname_ template. | `nil`                               |
| `controller.image.repository`             | Image repository for the controller image.                                                                                       | `ngrinder/controller`               |
| `controller.image.tag`                    | Image tag for the controller image.                                                                                              | `{{ .Chart.AppVersion }}`           |
| `controller.image.pullPolicy`             | Image pull policy for the controller image.                                                                                      | `IfNotPresent`                      |
| `controller.image.pullSecrets`            | Image pull secrets for the controller image.                                                                                     | `[]`                                |
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
| `controller.persistence.enabled`          | If `true`, create a PVC for controller.                                                                                          | `false`                             |
| `controller.persistence.annotations`      | Annotations to add to the PVC for controller.                                                                                    | `{}`                                |
| `controller.persistence.existingClaim`    | Use an existing PVC to persist data for controller.                                                                              | `nil`                               |
| `controller.persistence.accessMode`       | Persistence access mode for controller.                                                                                          | `ReadWriteOnce`                     |
| `controller.persistence.storageClass`     | PVC storage class for controller (use `-` for default).                                                                          | `standard`                          |
| `controller.persistence.size`             | Size of PVC to create for controller.                                                                                            | `8Gi`                               |
| `controller.resources`                    | Resource requests and limits for the primary controller container.                                                               | `{}`                                |
| `controller.nodeSelector`                 | Node labels for controller pod assignment.                                                                                       | `{}`                                |
| `controller.tolerations`                  | Toleration labels for controller pod assignment.                                                                                 | `[]`                                |
| `controller.affinity`                     | Affinity settings for controller pod assignment.                                                                                 | `{}`                                |
| `controller.config`                       | Config for all containers in the controller pod.                                                                                 | `{}`                                |
| `agent.maxReplicas`                       | Maxium number of agent pods.                                                                                                     | `10`                                |
| `agent.image.repository`                  | Image repository for the agent image.                                                                                            | `ngrinder/agent`                    |
| `agent.image.tag`                         | Image tag for the agent image.                                                                                                   | `{{ .Chart.AppVersion }}`           |
| `agent.image.pullPolicy`                  | Image pull policy for the agent image.                                                                                           | `IfNotPresent`                      |
| `agent.image.pullSecrets`                 | Image pull secrets for the agent image.                                                                                          | `[]`                                |
| `agent.podAnnotations`                    | Annotations to add to the agent pod.                                                                                             | `{}`                                |
| `agent.podLabels`                         | Labels to add to the agent pod.                                                                                                  | `{}`                                |
| `agent.podSecurityContext`                | Security context for the agent pod.                                                                                              | `{}`                                |
| `agent.securityContext`                   | Security context for the primary agent container.                                                                                | `{}`                                |
| `agent.priorityClassName`                 | Priority class name to use for agent pod.                                                                                        | `""`                                |
| `agent.resources`                         | Resource requests and limits for the primary agent container.                                                                    | `{}`                                |
| `agent.nodeSelector`                      | Node labels for agent pod assignment.                                                                                            | `{}`                                |
| `agent.tolerations`                       | Toleration labels for agent pod assignment.                                                                                      | `[]`                                |
| `agent.affinity`                          | Affinity settings for agent pod assignment.                                                                                      | `{}`                                |