# -*- coding:utf-8 -*-
"""
@author: ‘ch4r0n‘
@contact: xingrenchan@gmail.com
@site: 
@software: PyCharm
@file: logindb.py
@time: 2018/10/8 上午12:00
"""
from pony.orm import *
from .const import Constant
import os

db = Database()
db.bind(provider='sqlite', filename=os.path.join(Constant.conf_dir, "ncmusicapi.db"),create_db=True)
class Login_info(db.Entity):
    id = PrimaryKey(int, auto=True)
    phone = Optional(str)
    userId = Optional(int)
    Cookie = Optional(str)
    nickname = Optional(str)
db.generate_mapping(create_tables=True)

@db_session
def createSomeOne():
    p1 = Login_info(userId='123',Cookie="123123",nickname="myname")
    commit()

@db_session
def deleteAll():
    delete(p for p in Login_info)
    commit()

@db_session
def getSomeOneWithUserID(userid):
    p1 = Login_info.get(userId=userid)
    return p1

@db_session
def getSomeOneWithPhone(phone):
    p1 = Login_info.get(phone=phone)
    return p1

@db_session
def updateSomeOneCookiesWithPhone(phone, Cookie):
    p1 = getSomeOneWithPhone(phone)[0]
    p1.Cookie = Cookie
    commit()

@db_session
def createOne(phone, userId, Cookie, nickname):
    p1 = Login_info(userId=userId, Cookie=Cookie, phone=phone, nickname=nickname)
    commit()

@db_session
def updateOrInsertOne(phone, userId, Cookie, nickname):
    if Login_info.exists(userId=userId):
        puser = Login_info.get(userId=userId)
        puser.Cookie = Cookie
        puser.phone = phone
        puser.nickname = nickname
    else:
        createOne(phone,userId,Cookie, nickname)
