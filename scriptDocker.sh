#!/bin/bash
echo "######################"
echo "Starting KiboDB Docker"
echo "######################"
echo ""

if [ "$(docker ps -a | grep kibodb-run)" ]
then 
    echo "Docker kibodb already running"
    echo ""
    echo "Docker rm kibodb-run: "
    echo ""
    docker rm kibodb-run
fi

echo "Docker build : "
echo ""
docker build . --tag kibodb

echo ""
echo "Docker run : "
echo ""
docker run --name kibodb-run -p 8500:8500 -d kibodb

echo "Done"

docker logs kibodb-run

