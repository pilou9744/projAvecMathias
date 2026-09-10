@echo off

set "image_name=monapp"
set "container_id="

for /f "tokens=1" %%A in ('docker ps -a --filter "ancestor=%image_name%" --format "{{.ID}}"') do (
    set "container_id=%%A"
)

if defined container_id (
    echo Conteneur utilisant l'image %image_name% trouve.
    echo Demarrage du conteneur %container_id%...
    docker start -a %container_id%
) else (
    echo Aucun conteneur utilisant l'image %image_name% trouve.
    echo Construction de l'image...
    docker build -t %image_name% ./docker-app

    echo Lancement de l'application...
    docker run %image_name%
)

pause