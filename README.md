<p align="left">
    <a href="https://github.com/chpark-ML/boilerplate_pytorch/actions">
      <img alt="Tests Passing" src="https://github.com/chpark-ML/boilerplate_pytorch/actions/workflows/pylint.yml/badge.svg" />
    </a>
    <a href="https://github.com/chpark-ML/boilerplate_pytorch/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/chpark-ML/boilerplate_pytorch?color=0088ff" />
    </a>
    <a href="https://github.com/chpark-ML/boilerplate_pytorch/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/chpark-ML/boilerplate_pytorch?color=0088ff">
    </a>
</p>


# PyTorch boilerplate, MNIST 🚗
MNIST 데이터셋을 통해서 분류 문제를 학습하는 딥러닝 모델 학습 파이프라인입니다.

***
## Overview of project 👍
- **dockerfile** (docker build context)
- **makefile** (docker build handler)
- **project** (model training project)
    - train.py
    - train_test.py
    - utils
        - dataset.py
        - model.py
        - util.py
    - configs

***
## DockerFile & DockerCompose 👍
도커를 활용한 개발환경 구축은 다음 링크를 참조하여 작성되었음. [Cresset](https://github.com/cresset-template/cresset)

### 1. How to build a development environment
```
make env
make build-dev
make exec-dev
```

**`make env`**
- docker build context (`./dockerfile`) 내부에 `.env` 파일을 생성하고 도커 이미지 빌드를 위한 변수들을 저장

**`make build-dev`**
- 도커 개발 서비스를 구축하기 위한 명령문
- makefile에 정의된 dependency에 따라 docker base image를 빌드한 뒤, development docker image 빌드 수행

**`make exec-dev`**
- 빌드 된 도커 이미지를 통해 docker container를 생성하고 실행

***
## Project 👍

MNIST 데이터셋을 학습하고 분류 문제를 푸는 딥러닝 모델 학습 파이프라인 예제 코드입니다.

### 1. Model training
```
python3 train.py
```