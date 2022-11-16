# Hello Python

Very simple hello world python Flask application for deploying to k8s.

## Important commands


# Apply changes to k8s
kubectl apply -f ../kubernetes/deployment.yaml

Authorize with:
`gcloud auth configure-docker us-central1-docker.pkg.dev`

To build the file, cd to the app directory and type:
`docker build -f ../docker/Dockerfile -t us-central1-docker.pkg.dev/sandbox-service-2/craven-repository/hello-python:latest .`

To run the image and map the port:
`docker run -p 8080:5000 us-central1-docker.pkg.dev/sandbox-service-2/craven-repository/hello-python:latest`

Push:
`docker push us-central1-docker.pkg.dev/sandbox-service-2/craven-repository/hello-python:latest`
