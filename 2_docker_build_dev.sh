# How to run, e.g., sh docker_2_build_dev.sh
docker build \
 --tag project:dev_${USER} \
 -f ./dockerFile/Dockerfile_base . \
 --build-arg USER_ID=$(id -u ${USER}) \
 --build-arg GRUOP_ID=$(id -g ${USER})