docker_name=monapp

ps=`docker ps -a | grep $docker_name`

image=`echo $ps | awk '{print $2}'`

container_id=`echo $ps | awk '{print $1}'`

if [ "$image" = "$docker_name" ]
then
    docker start $container_id
else
    docker build -t $docker_name ./docker-app
    docker run $docker_name
fi