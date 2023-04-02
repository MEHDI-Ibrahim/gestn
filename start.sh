#!/bin/bash

# Define variables
DOCKER_REGISTRY="localhost:5000"
FAKER_IMAGE="faker"
BD_IMAGE="bd"
LOGIN_IMAGE="login"
NOTES_IMAGE="notes"

# Build each Docker image
docker build -t $FAKER_IMAGE -f faker/Dockerfile .
docker build -t $BD_IMAGE -f bd/Dockerfile .
docker build -t $LOGIN_IMAGE -f login/Dockerfile .
docker build -t $NOTES_IMAGE -f notes/Dockerfile .

# Create a Docker container for the registry
docker run -d -p 5000:5000 --name registry registry:2

# Tag and push each Docker image to the registry
docker tag $FAKER_IMAGE $DOCKER_REGISTRY/$FAKER_IMAGE
docker push $DOCKER_REGISTRY/$FAKER_IMAGE

docker tag $BD_IMAGE $DOCKER_REGISTRY/$BD_IMAGE
docker push $DOCKER_REGISTRY/$BD_IMAGE

docker tag $LOGIN_IMAGE $DOCKER_REGISTRY/$LOGIN_IMAGE
docker push $DOCKER_REGISTRY/$LOGIN_IMAGE

docker tag $NOTES_IMAGE $DOCKER_REGISTRY/$NOTES_IMAGE
docker push $DOCKER_REGISTRY/$NOTES_IMAGE
