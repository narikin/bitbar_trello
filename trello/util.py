#!/usr/bin/env python
# -*- coding: utf-8 -*-


import configparser
import sys


def get_config(path):
    """ Get config object """
    config = configparser.ConfigParser()

    try:
        config.read(path)
        return config
    except Exception as e:
        print(e)
        sys.exit(1)
