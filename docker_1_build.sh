# How to run, e.g., sh docker_1_build.sh
docker build \
 --tag project:dev_${USER} \
 -f ./docker/Dockerfile_base . \
 --build-arg USER_ID=$(id -u ${USER}) \
 --build-arg GRUOP_ID=$(id -g ${USER})