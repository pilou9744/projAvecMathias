#!/bin/sh

image_name=monapp
container_id=$(docker ps -aq --filter "ancestor=$image_name" | head -n 1)

if [ -n "$container_id" ]; then
    echo "Conteneur utilisant l'image $image_name trouve."
    echo "Demarrage du conteneur $container_id..."
    docker start -a "$container_id"
else
    echo "Aucun conteneur utilisant l'image $image_name trouve."
    echo "Construction de l'image..."
    docker build -t "$image_name" ./docker-app || exit $?

    echo "Lancement de l'application..."
    docker run "$image_name"
fi
