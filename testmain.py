# -*- coding:utf-8 -*-
"""
@author: ‘ch4r0n‘
@contact: xingrenchan@gmail.com
@site: 
@software: PyCharm
@file: testmain.py
@time: 2018/10/16 下午10:26
"""
from NCMusicAPI.musicAPI import *


if __name__ == '__main__':
    net = NeteaseAdapter("http://192.168.50.230:3000")
    print net.login("aaa","aaa")

