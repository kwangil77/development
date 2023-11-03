{{/* vim: set filetype=mustache: */}}
{{/*
Create a default fully qualified app name.
*/}}
{{- define "ngrinder.controller.fullname" -}}
{{ include "ngrinder.fullname" . }}-controller
{{- end }}

{{/*
Common labels
*/}}
{{- define "ngrinder.controller.labels" -}}
{{ include "ngrinder.labels" . }}
app.kubernetes.io/component: controller
{{- end }}

{{/*
Selector labels
*/}}
{{- define "ngrinder.controller.selectorLabels" -}}
{{ include "ngrinder.selectorLabels" . }}
app.kubernetes.io/component: controller
{{- end }}

{{/*
Create pvc name.
*/}}
{{- define "ngrinder.controller.pvcname" -}}
{{- template "ngrinder.controller.fullname" . -}}-data
{{- end -}}

{{/* Fix KubeVersion with bad pre-release. */}}
{{- define "ngrinder.controller.kubeVersion" -}}
  {{- default .Capabilities.KubeVersion.Version (regexFind "v[0-9]+\\.[0-9]+\\.[0-9]+" .Capabilities.KubeVersion.Version) -}}
{{- end -}}

{{/* Get Ingress API Version */}}
{{- define "ngrinder.controller.ingress.apiVersion" -}}
  {{- if and (.Capabilities.APIVersions.Has "networking.k8s.io/v1") (semverCompare ">= 1.19.x" (include "ngrinder.controller.kubeVersion" .)) -}}
      {{- print "networking.k8s.io/v1" -}}
  {{- else if .Capabilities.APIVersions.Has "networking.k8s.io/v1beta1" -}}
    {{- print "networking.k8s.io/v1beta1" -}}
  {{- else -}}
    {{- print "extensions/v1beta1" -}}
  {{- end -}}
{{- end -}}

{{/* Check Ingress stability */}}
{{- define "ngrinder.controller.ingress.isStable" -}}
  {{- eq (include "ngrinder.controller.ingress.apiVersion" .) "networking.k8s.io/v1" -}}
{{- end -}}

{{/* Check Ingress supports pathType */}}
{{/* pathType was added to networking.k8s.io/v1beta1 in Kubernetes 1.18 */}}
{{- define "ngrinder.controller.ingress.supportsPathType" -}}
  {{- or (eq (include "ngrinder.controller.ingress.isStable" .) "true") (and (eq (include "ngrinder.controller.ingress.apiVersion" .) "networking.k8s.io/v1beta1") (semverCompare ">= 1.18.x" (include "ngrinder.controller.kubeVersion" .))) -}}
{{- end -}}