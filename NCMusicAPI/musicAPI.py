# -*- coding:utf-8 -*-
"""
@author: ‘ch4r0n‘
@contact: xingrenchan@gmail.com
@site: 
@software: PyCharm
@file: musicAPI.py
@time: 2018/10/7 下午8:35
"""
import requests
import json
from .const import Constant


default_timeout = 10

class NeteaseAdapter(object):
    def __init__(self):
        self.header = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'http://music.163.com/search/',
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'  # NOQA
        }
        self.cookies = ''
        self.playlist_class_dict = {}
        self.session = requests.Session()

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

        elif method == 'Login_GET':
            url = action if query is None else action + '?' + query
            connection = self.session.get(url,
                                          headers=self.header,
                                          timeout=default_timeout)
            self.cookies = connection.headers['Set-Cookie']
        # print self.session.cookies.clear()
        connection.encoding = 'UTF-8'
        return connection.text

    # 登陆
    def login(self,username,password):
        '''
        进行登陆操作,只支持手机号
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        action = Constant.host + "/login/cellphone?phone=%s&password=%s" % (username, password)
        try:
            return self.httpRequest("Login_GET", action)
        except Exception,e:
            print e
            return {"code": 501}
    # 搜索歌曲
    def search(self, song_name, limit):
        '''
        搜索歌曲操作,默认返回一串json
        :param song_name: 歌名
        :return: json
        '''
        action = Constant.host + "/search?keywords=%s&limit=%d" % (song_name,limit)
        try:
            return self.httpRequest("GET", action)
        except Exception,e:
            print e
            return {"code": 501}

    # song ids --> song urls ( details )
    def songs_detail(self, ids, offset=0):
        tmpids = ids[offset:]
        tmpids = tmpids[0:100]
        tmpids = list(map(str, tmpids))
        action = 'http://music.163.com/api/song/detail?ids=[{}]'.format(  # NOQA
            ','.join(tmpids))
        try:
            data = self.httpRequest('GET', action)
            # the order of data['songs'] is no longer the same as tmpids,
            # so just make the order back
            data['songs'].sort(key=lambda song: tmpids.index(str(song['id'])))
            return data['songs']
        except requests.exceptions.RequestException as e:
            print e
            return []

    # 将songs拼接为song_info
    # 并且将id转换为url
    def transfer_song_info(self, songs):
        '''
        songs为一坨
        :param songs:
        :return: songs_info
        song_info = {
                    'song_id': data[i]['id'],
                    'artist': [],
                    'song_name': data[i]['name'],
                    'album_name': album_name,
                    'album_id': album_id,
                    'mp3_url': url,
                    'quality': quality,
                    'playTime': play_time
                }
        '''
        song_list = []
        song_info = {}
        for song_item in songs:
            song_info['song_id'] = song_item['id']
            song_info['artist'] = song_item['artists']
            song_info['song_name'] = song_item['name']
            song_info['album_name'] = song_item['album']['name']
            song_info['album_id'] = song_item['album']['id']
            song_url_data = self.song_id_to_url(song_item['id'])
            song_info['mp3_url'] = song_url_data['data'][0]['url']
            song_info['quality'] = song_url_data['data'][0]['br']
            song_info['playTime'] = song_item['duration']
            song_list.append(song_info)
        return song_list

    # 获取song的url
    def song_id_to_url(self,song_id):
        '''
        获取song的url
        :param song_id:
        :return:
        '''
        action = Constant.host + "/music/url?id=%d" % song_id
        try:
            return self.httpRequest("GET", action)
        except Exception,e:
            print e
            return {"code": 501}

    #登陆状态查询
    def login_status(self):
        action = Constant.host + "/login/status"
        try:
            return self.httpRequest("GET",action)
        except Exception,e:
            return {"code": 501}



if __name__ == '__main__':
    print "hello world"
    na = NeteaseAdapter()
    # print na.search("海阔天空",2)
    songs = [{u'album': {u'status': 3, u'copyrightId': 7002, u'name': u'\u534e\u7eb323\u5468\u5e74\u7eaa\u5ff5\u7cbe\u9009\u7cfb\u5217', u'artist': {u'img1v1Url': u'http://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg', u'name': u'', u'albumSize': 0, u'alias': [], u'picId': 0, u'img1v1': 0, u'picUrl': None, u'trans': None, u'id': 0}, u'publishTime': 999273600007, u'picId': 3273246124149810, u'id': 34430029, u'size': 14}, u'status': 0, u'copyrightId': 7002, u'name': u'\u6d77\u9614\u5929\u7a7a', u'rtype': 0, u'fee': 8, u'mvid': 0, u'alias': [], u'ftype': 0, u'artists': [{u'img1v1Url': u'http://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg', u'name': u'Beyond', u'albumSize': 0, u'alias': [], u'picId': 0, u'img1v1': 0, u'picUrl': None, u'trans': None, u'id': 11127}], u'duration': 323693, u'rUrl': None, u'id': 400162138}, {u'album': {u'status': 1, u'copyrightId': 0, u'name': u'\u6d77\u9614\u5929\u7a7a', u'artist': {u'img1v1Url': u'http://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg', u'name': u'', u'albumSize': 0, u'alias': [], u'picId': 0, u'img1v1': 0, u'picUrl': None, u'trans': None, u'id': 0}, u'publishTime': 1075564800000, u'picId': 109951163028211129, u'id': 38408, u'size': 10}, u'status': 0, u'copyrightId': 489015, u'name': u'\u6d77\u9614\u5929\u7a7a', u'rtype': 0, u'fee': 8, u'mvid': 5343895, u'alias': [], u'ftype': 0, u'artists': [{u'img1v1Url': u'http://p1.music.126.net/6y-UleORITEDbvrOLV0Q8A==/5639395138885805.jpg', u'name': u'\u4fe1\u4e50\u56e2', u'albumSize': 0, u'alias': [], u'picId': 0, u'img1v1': 0, u'picUrl': None, u'trans': None, u'id': 13283}], u'duration': 278936, u'rUrl': None, u'id': 387717}]
    print na.transfer_song_info(songs=songs)
    # print songs






