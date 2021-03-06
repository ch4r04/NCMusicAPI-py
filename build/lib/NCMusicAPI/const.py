# -*- coding:utf-8 -*-
"""
@author: ‘ch4r0n‘
@contact: xingrenchan@gmail.com
@site: 
@software: PyCharm
@file: const.py
@time: 2018/10/7 下午11:07
"""
import os


class Constant(object):
    conf_dir = os.path.join(os.path.expanduser('~'), '.netease-musicbox')
    download_dir = os.path.join(conf_dir, 'cached')
    config_path = os.path.join(conf_dir, 'config.json')
    storage_path = os.path.join(conf_dir, 'database.json')
    cookie_path = os.path.join(conf_dir, 'cookie')
    log_path = os.path.join(conf_dir, 'musicbox.log')
    host = "http://localhost:3000"
