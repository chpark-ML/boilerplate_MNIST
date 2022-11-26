echo "------------------------------"
echo "start stopping"
docker stop `docker ps -a -q`
echo "------------------------------"
echo "start removing"
docker rm `docker ps -a -q`
echo "------------------------------"