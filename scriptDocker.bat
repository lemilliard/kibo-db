echo "##########################"
echo "# Starting KiboDB Docker #"
echo "##########################"
echo ""

REM if [docker ps -a | findstr 'kibodb-run'] (
REM     echo "Docker kibodb already running"
REM     echo ""

REM     echo "Docker rm kibodb-run: "
REM     echo ""
REM     docker rm -f kibodb-run
REM     echo ""

REM     echo "Docker rmi kibodb"
REM     echo ""
REM     docker rmi -f kibodb
REM     echo ""
REM )

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


if not exist "%cd%\data\" mkdir %cd%\data
if not exist "%cd%\data\kibodb" mkdir %cd%\data\kibodb
if not exist "%cd%\data\kibodb\databases" mkdir %cd%\data\kibodb\databases

echo ""
echo "##############"
echo "# Docker run #"
echo "##############"
echo ""

docker run -v %cd%/data/kibodb/databases:/usr/src/databases --name kibodb-run -p 8500:8500 -d kibodb

echo ""
echo "#########################"
echo "# KiboDB is now running #"
echo "#########################"
echo ""

docker logs kibodb-run

