# -*- coding: utf-8 -*-
"""this is sample code of configparser module.

http://inner2.hatenablog.com/entry/2015/12/01/211329
"""

import configparser

config = configparser.ConfigParser()
config.read('./config.ini')

print(config['system']['os'])
print(config['user']['name'])


# writing

default = {'user': 'inner'}
info = {'directory': 'dir', 'mode': 0}

config = configparser.ConfigParser()
config['default'] = default
config['info'] = info

with open('config.txt', 'w') as configfile:
    config.write(configfile)
