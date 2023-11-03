{{/* vim: set filetype=mustache: */}}
{{/*
Create a default fully qualified app name.
*/}}
{{- define "boundary.controller.fullname" -}}
{{ include "boundary.fullname" . }}-controller
{{- end }}

{{/*
Common labels
*/}}
{{- define "boundary.controller.labels" -}}
{{ include "boundary.labels" . }}
app.kubernetes.io/component: controller
{{- end }}

{{/*
Selector labels
*/}}
{{- define "boundary.controller.selectorLabels" -}}
{{ include "boundary.selectorLabels" . }}
app.kubernetes.io/component: controller
{{- end }}

{{/* Fix KubeVersion with bad pre-release. */}}
{{- define "boundary.controller.kubeVersion" -}}
  {{- default .Capabilities.KubeVersion.Version (regexFind "v[0-9]+\\.[0-9]+\\.[0-9]+" .Capabilities.KubeVersion.Version) -}}
{{- end -}}

{{/* Get Ingress API Version */}}
{{- define "boundary.controller.ingress.apiVersion" -}}
  {{- if and (.Capabilities.APIVersions.Has "networking.k8s.io/v1") (semverCompare ">= 1.19.x" (include "boundary.controller.kubeVersion" .)) -}}
      {{- print "networking.k8s.io/v1" -}}
  {{- else if .Capabilities.APIVersions.Has "networking.k8s.io/v1beta1" -}}
    {{- print "networking.k8s.io/v1beta1" -}}
  {{- else -}}
    {{- print "extensions/v1beta1" -}}
  {{- end -}}
{{- end -}}

{{/* Check Ingress stability */}}
{{- define "boundary.controller.ingress.isStable" -}}
  {{- eq (include "boundary.controller.ingress.apiVersion" .) "networking.k8s.io/v1" -}}
{{- end -}}

{{/* Check Ingress supports pathType */}}
{{/* pathType was added to networking.k8s.io/v1beta1 in Kubernetes 1.18 */}}
{{- define "boundary.controller.ingress.supportsPathType" -}}
  {{- or (eq (include "boundary.controller.ingress.isStable" .) "true") (and (eq (include "boundary.controller.ingress.apiVersion" .) "networking.k8s.io/v1beta1") (semverCompare ">= 1.18.x" (include "boundary.controller.kubeVersion" .))) -}}
{{- end -}}