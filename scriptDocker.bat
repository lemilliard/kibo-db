@echo off
echo "##########################"
echo "# Starting KiboDB Docker #"
echo "##########################"
echo ""

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


if not exist "C:\kibodb" mkdir C:\kibodb
if not exist "C:\kibodb\databases" mkdir C:\kibodb\databases

echo ""
echo "##############"
echo "# Docker run #"
echo "##############"
echo ""

docker run -v C:/kibodb/databases:/usr/src/databases --name kibodb-run -p 8500:8500 -d kibodb

echo ""
echo "#########################"
echo "# KiboDB is now running #"
echo "#########################"
echo ""

docker logs kibodb-run

