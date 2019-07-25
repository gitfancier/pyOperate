#!/bin/python
from fabric.api import hosts, env, run,local


def preparedeploy():
    local('git')

if __name__ == "__main__":
    preparedeploy();