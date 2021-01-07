# Simple Python flask app
Features:  
* reverse proxy with multiple strategies: roundrobin, random
* allows load balancing over multiple backend services
* can use authentication with local postgres database
* exposes a static accounts_pages page used to visualize users from the database
* exposes /metrics endpoint for prometheus scraping
* there is a short test http web servers script which implements the backend services
* there is also a test script used to populate the database with accounts
* can be deployed in minikube using helm
* can be deployed in docker using docker-compose

# Prerequisites
* Install helm, minikube and have docker running
* Git clone repository

## Deployment
### Deploy with minikube
1. Have minikube up and running
```shell script
minikube start
```

2. Change directory to `app/deploy/helm`
```shell script
cd app/deploy/helm
```

3. Execute helm install command
```shell script
helm install  ./appchart --name app --namespace app
```
The app should now be up and running
To test the app follow the next steps:
1. Obtain the minikube IP:
```shell script
minikube ip
```

2. Change the `/etc/hosts` file and point the app services to this ip. (Note that the app uses the `app.yaml` config 
file in which we specify backend services) e.g.:
```shell script
192.168.99.105 service1.my-company.com
192.168.99.105 service2.my-company.com
```
You should now be able to access the app

### Deploy with docker-compose
1. Change directory to `app/deploy/docker-compose`
```shell script
cd app/deploy/docker-compose
```

2. Execute `docker-compose` command to start containers on the local machine:
```shell script
docker-compose up -d
```
Containers should now be up and running, check them using `docker ps` command
You should now be able to access the app

## Accessing the app
Make sure that the /etc/hosts file point to the correct endpoints for backend services:

Note: If authentication is used (specified in config file) then you need to create a new account before using the app.
* Creating a new account:
Execute a POST call on `http://localhost:8080/account` with the following body:
```json
{
    "username": "user",
    "password": "user",
    "email": "user3@test.com"
}
```
* Login with account
Execute a POST call on `http://localhost:8080/login` with the following body:
```json
{
    "password": "user",
    "email": "user3@test.com"
}
```
A JWT token will be returned if authentication is successful. 

* Proxy data to backend services:
Execute a POST request to `http://service2.my-company.com:8080` or `http://service1.my-company.com:8080` and make sure
to add the 'Authorization' header and use the JWT token

* Checking the database accounts page. The app exposes a simple page that fetches accounts from the postgres database 
and displays them. Checkout the `http://localhost:8080/accounts_page`

### SLI/app metrics
The app exposes a `/metrics` endpoint that can be scraped by Prometheus and implements alerts based on metrics:
`http://localhost:8080/metrics`

**Reliability**  
Each request exposes a `flask_http_request_duration_seconds_count` which counts the request time  
There is also a `flask_http_request_duration_seconds_count` and `flask_http_request_duration_seconds_sum` that can be used   
to determine the 5xx and 2xx from the number of requests (e.g 5xx flask_http_request_duration_seconds_sum / flask_http_request_duration_seconds_count)  

**Availability**  
Can be calculated by checking the number of 2xx responses for 1 minute interval over a 30 day period  
This can be calculated for each backend services and the frontend proxy  

**Scalability**  
The app exposes cpu and memory which can be taken into consideration when increasing the number of replicas by using
horizontal pod autoscaler in Kubernetes. This determines the max allowed load on a given pod.  
Another solution would be to build a custom autoscaler controller that takes into account the number of requests per endpoint
which could trigger a pod scale
