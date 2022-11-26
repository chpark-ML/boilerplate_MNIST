echo "------------------------------"
echo "start removing"
docker rmi `docker images -a -q`