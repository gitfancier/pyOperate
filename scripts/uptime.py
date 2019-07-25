#!/bin/python

from fabric.api import local


def uptime():
    local('uptime');

if __name__ == "__main__":
    uptime();