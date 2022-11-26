# How to run, e.g., sh docker_2_run.sh dev_chpark
#!/bin/bash
docker run \
 -it \
 --shm-size=1g \
 --ulimit memlock=-1 \
 -v $pwd:/usr/src/project \
 -v /data_hdd:/data_hdd \
 -v /data_ssd:/data_ssd \
 --name $1 project:$1
