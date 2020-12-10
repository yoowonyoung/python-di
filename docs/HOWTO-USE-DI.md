# DI
DI + Module

## Prerequisites

### Python3 (^3.7.0)
    sudo apt install python3 python3-pip

### Install python libs
    pip3 install -Ur requirments.txt

## How to use
Set environment variable if you want to run script without credentials and server info

    export DI_EXAMPLE_MYSQL_HOST=MYSQL_HOST_PLACEHOLDER
    export DI_EXAMPLE_MYSQL_PORT=3306
    export DI_EXAMPLE_MYSQL_DATABASE=MYSQL_DATABAES_PLACEHOLDER
    export DI_EXAMPLE_MYSQL_USERNAME=MYSQL_USERNAME_PLACEHOLDER
    export DI_EXAMPLE_MYSQL_PASSWORD=MYSQL_PASSWORD_PLACEHOLDER

Run script

    python3 -m sedafw.refinery.xxx xxx 2020 9
