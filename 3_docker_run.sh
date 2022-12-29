# How to run, e.g., sh 3_docker_run.sh
#!/bin/bash
docker run \
 -it \
 --shm-size=10g \
 --ulimit memlock=-1 \
 -v $pwd:/usr/src/project \
 -v /data_hdd:/data_hdd \
 -v /data_ssd:/data_ssd \
 --name dev_${USER} project:dev_${USER}
