echo "------------------------------"
echo "start removing"
docker rmi -f `docker images -a -q`
