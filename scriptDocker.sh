#!/bin/bash
echo "##########################"
echo "# Starting KiboDB Docker #"
echo "##########################"
echo ""

if [ "$(docker ps -a | grep kibodb-run)" ]
then
    echo "Docker kibodb already running"
    echo ""

    echo "Docker rm kibodb-run: "
    echo ""
    docker rm -f kibodb-run
    echo ""

    echo "Docker rmi kibodb"
    echo ""
    docker rmi -f kibodb
    echo ""
fi

echo ""
echo "################"
echo "# Docker build #"
echo "################"
echo ""

docker build . --tag kibodb

echo ""
echo "#################"
echo "# Creating dirs #"
echo "#################"
echo ""

mkdir /var/kibodb
mkdir /var/kibodb/databases

echo ""
echo "##############"
echo "# Docker run #"
echo "##############"
echo ""

docker run -v /var/kibodb/databases:/usr/src/databases --name kibodb-run -p 8500:8500 -d kibodb

echo ""
echo "#########################"
echo "# KiboDB is now running #"
echo "#########################"
echo ""

docker logs kibodb-run

