# boilerplate_MNIST

## Overview of project
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


## DockerFile & DockerCompose
도커를 활용한 개발환경 구축은 다음 링크를 참조하여 작성되었음. [Cresset](https://github.com/cresset-template/cresset)

### 1. How to start docker
    ```
    make env
    make build-dev
    make exec-dev
    ```
