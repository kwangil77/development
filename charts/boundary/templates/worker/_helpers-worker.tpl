{{/* vim: set filetype=mustache: */}}
{{/*
Create a default fully qualified app name.
*/}}
{{- define "boundary.worker.fullname" -}}
{{ include "boundary.fullname" . }}-worker
{{- end }}

{{/*
Common labels
*/}}
{{- define "boundary.worker.labels" -}}
{{ include "boundary.labels" . }}
app.kubernetes.io/component: worker
{{- end }}

{{/*
Selector labels
*/}}
{{- define "boundary.worker.selectorLabels" -}}
{{ include "boundary.selectorLabels" . }}
app.kubernetes.io/component: worker
{{- end }}