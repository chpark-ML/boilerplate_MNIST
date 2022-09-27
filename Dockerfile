FROM pytorch/pytorch
MAINTAINER jylee
LABEL "purpose"="test"
RUN pip install pandas
RUN echo hello
WORKDIR /home
