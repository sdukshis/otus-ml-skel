# Guide for install kube-prometheus-stack

## Documentataion
https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack

## Install prometheus-community:
- ```helm repo add prometheus-community https://prometheus-community.github.io/helm-charts```


- ```helm repo update```


- ```helm install monitoring prometheus-community/kube-prometheus-stack```

'monitoring' -> my release name for prometheus


## Set service
**Deploy service**
- ```kubectl apply -f k8s/ititanic-deployment.yml```

**Run prometheus service**
- ```kubectl apply -f k8s/titanic-service.yml```

**Run monitoring service**
- ```kubectl apply -f k8s/monitoring-titanic.yml```

**Set rbac**
- ```kubectl apply -f k8s/prom_rbac.yml```


## Forward ports
**Prometheus**
- ```kubectl port-forward svc/prometheus-operated 9090:9090 -n default```
check -> http://127.0.0.1:9090/

**Grafana**
- ```kubectl port-forward svc/monitoring-grafana 8082:80 -n default```
check -> http://127.0.0.1:8082/

## Forward service ports
- ```kubectl get pods```
- ```kubectl port-forward <titanic pods name> 8000:8000 -n default```
check -> 127.0.0.1:8000
check -> 127.0.0.1:8000/metrics

## Send request

- ```python service/send_request.py```
