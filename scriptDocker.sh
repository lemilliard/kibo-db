#!/bin/bash
echo "######################"
echo "Starting KiboDB Docker"
echo "######################"
echo ""

if [ "$(docker ps -a | grep kibodb-run)" ]
then 
    echo "Docker mongo already running"
    echo "Please run 'docker rm kibodb-run' before running this script"
else
    echo "Docker build : "
    echo ""
    docker build . --tag kibodb

    echo ""
    echo "Docker run : "
    echo ""
    docker run --name kibodb-run -p 8500:8500 -d kibodb

    echo "Done"

    docker logs kibodb-run
fi
