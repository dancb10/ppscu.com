#!/usr/bin/env bash
set -e
set -x

IMAGE_NAME=backend
VERSION=latest

docker build -f test/Dockerfile -t $IMAGE_NAME:$VERSION .
docker tag $IMAGE_NAME:$VERSION docker.io/dancb10/$IMAGE_NAME:$VERSION
