#!/bin/bash

# Define variables
DOCKER_REGISTRY="localhost:5000"
BD_IMAGE="bd"
LOGIN_IMAGE="login"
NOTES_IMAGE="notes"

# Build each Docker image
docker build -t $BD_IMAGE -f bd/Dockerfile .
docker build -t $LOGIN_IMAGE -f login/Dockerfile .
docker build -t $NOTES_IMAGE -f notes/Dockerfile .

docker run -u 0 --privileged --name jenkins -d -p 8080:8080 -p 50000:50000 -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker -v /home/jenkins_home:/jenkinsData jenkins/jenkins:latest

# Create a Docker container for the registry

docker run -d -p 5000:5000 --name registry registry:2

# Tag and push each Docker image to the registry

docker tag $BD_IMAGE $DOCKER_REGISTRY/$BD_IMAGE
docker push $DOCKER_REGISTRY/$BD_IMAGE

docker tag $LOGIN_IMAGE $DOCKER_REGISTRY/$LOGIN_IMAGE
docker push $DOCKER_REGISTRY/$LOGIN_IMAGE

docker tag $NOTES_IMAGE $DOCKER_REGISTRY/$NOTES_IMAGE
docker push $DOCKER_REGISTRY/$NOTES_IMAGE



#Deploy

kubectl apply -f application.yaml