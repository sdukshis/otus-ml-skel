Последовательность моих шагов такая:

1. `kubectl apply -f k8s/prom_rbac.yml`
2. `kubectl apply -f k8s/titanic-deployment.yml`
3. `kubectl apply -f k8s/monitoring-titanic.yml`
4. `helm repo add prometheus-community https://prometheus-community.github.io/helm-charts`
5. `helm repo update`
6. `helm install prometheus prometheus-community/kube-prometheus-stack`

Дальше делаю port-forward для каждого из сервисов:
- `kubectl port-forward service/prometheus-operated 9090:9090`
- `kubectl port-forward service/prometheus-grafana 8080:80`
- `kubectl port-forward deploy/titanic-deployment 8000:8000`

Затем захожу на `http://localhost:9090/targets`, но метрик сервиса там нет (см. картинку bug_1 в корне репозитория). Хотя если открыть all scrape pools, то сервис титаника там есть (см. bug_2). При этом сам сервис титаника на localhost:8000 работает как надо, endpoint metrics есть.

Сам k8s поднят через docker v1.25.9

Поменял лишь только prob_rbac.yml, так как бета версия, которая указана в master ветке не запускается. Поставил просто версию 1


