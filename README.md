# Hello Python

Very simple hello world python Flask application for deploying to k8s.

## Important commands

To build the file, cd to the app directory and type:
`docker build -f ../docker/Dockerfile -t hello-python:latest .`

To run the image and map the port:
`docker run -p 5001:5000 hello-python`

Authorize with:
`gcloud auth configure-docker us-central1-docker.pkg.dev`

Tag:
`docker tag hello-python us-central1-docker.pkg.dev/sandbox-service-2/craven-repository`

Push:
`docker push us-central1-docker.pkg.dev/sandbox-service-2/craven-repository/hello-python`
