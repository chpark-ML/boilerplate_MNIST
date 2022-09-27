# base image를 ubuntu
# cuda version 확인하고 변수로 두기
FROM pytorch/pytorch
MAINTAINER jylee

# timezone TZ

LABEL "purpose"="test"

# libraries, essential
RUN pip install pandas

# libraries, the else

# Set variable for archive.ubuntu, mirror.kakao, etc.

# printf "/etc/pip.conf"

# libraries, high-level lib, tmux, git, pip, zsh, etc.

# set user, group

# requirement.txt

WORKDIR /home

# set ENV, enviromental variable

# install requirement

# CMD?