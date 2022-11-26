# How to run, e.g., sh docker_1_build_base.sh
docker build \
 --tag pytorch:dev_${USER} \
 -f ./dockerFile/Dockerfile_base . \
 --build-arg USER_ID=$(id -u ${USER}) \
 --build-arg GRUOP_ID=$(id -g ${USER})