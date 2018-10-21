# -*- coding:utf-8 -*-
"""
@author: ‘ch4r0n‘
@contact: xingrenchan@gmail.com
@site: 
@software: PyCharm
@file: utils.py
@time: 2018/10/7 下午8:38
"""
import json

default_timeout = 10

def httpRequest(self,
                method,
                action,
                query=None,
                urlencoded=None,
                callback=None,
                timeout=None):
    connection = json.loads(
        self.rawHttpRequest(method, action, query, urlencoded, callback, timeout)
    )
    return connection


def rawHttpRequest(self,
                   method,
                   action,
                   query=None,
                   urlencoded=None,
                   callback=None,
                   timeout=None):
    if method == 'GET':
        url = action if query is None else action + '?' + query
        connection = self.session.get(url,
                                      headers=self.header,
                                      timeout=default_timeout)

    elif method == 'POST':
        connection = self.session.post(action,
                                       data=query,
                                       headers=self.header,
                                       timeout=default_timeout)

    elif method == 'Login_POST':
        connection = self.session.post(action,
                                       data=query,
                                       headers=self.header,
                                       timeout=default_timeout)
        self.session.cookies.save()

    connection.encoding = 'UTF-8'
    return connection.text

