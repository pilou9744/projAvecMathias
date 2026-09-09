```bat
@echo off

set "docker_name=monapp"

for /f "tokens=1,2" %%A in ('docker ps -a --filter "name=%docker_name%" --format "{{.ID}} {{.Image}}"') do (
    set "container_id=%%A"
    set "image=%%B"
)

if "%image%"=="%docker_name%" (
    docker start %container_id%
) else (
    docker build -t %docker_name% ./docker-app
    docker run %docker_name%
)
```
