@echo off
set CONTAINER_NAME=monapp

docker container inspect %CONTAINER_NAME% >nul 2>&1

if %errorlevel%==0 (
echo Le conteneur %CONTAINER_NAME% existe deja.
echo Demarrage du conteneur...
docker start %CONTAINER_NAME%
) else (
echo Le conteneur %CONTAINER_NAME% n'existe pas.
echo Creation et demarrage du conteneur...
docker run -d --name %CONTAINER_NAME% monapp
)

echo.
echo Termine.
pause
