{{/* vim: set filetype=mustache: */}}
{{/*
Create a default fully qualified app name.
*/}}
{{- define "ngrinder.agent.fullname" -}}
{{ include "ngrinder.fullname" . }}-agent
{{- end }}

{{/*
Common labels
*/}}
{{- define "ngrinder.agent.labels" -}}
{{ include "ngrinder.labels" . }}
app.kubernetes.io/component: agent
{{- end }}

{{/*
Selector labels
*/}}
{{- define "ngrinder.agent.selectorLabels" -}}
{{ include "ngrinder.selectorLabels" . }}
app.kubernetes.io/component: agent
{{- end }}