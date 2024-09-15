# IPC
Series of py files to develop IPC mkfifo python routines

[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

![](header.png)

## Installation

Just need python installed and run these scripts from the linux command line

## Usage example

These examples will require 2 terminal windows to be open: one for the sender and another for the receiver

Terminal 1:
```sh
python receiver.py # default fifo is /tmp/my_fifo
```
Terminal 2:
```sh
python sender.py
```

## Release History

* 0.1.0
    * Initial implementation
