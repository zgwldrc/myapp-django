from django.test import TestCase

# Create your tests here.
import http.cookiejar, urllib.request
import json


class UserTest(TestCase):
    user_api = 'http://localhost:8000/api/user/'
    login_api = 'http://localhost:8000/api/login/'
    logout_api = 'http://localhost:8000/api/logout/'
    account_api = 'http://localhost:8000/api/account/'

    def test_001(self):

        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        urllib.request.install_opener(opener)

        req_map = {}

        data = json.dumps([{"model": "auth.user", "fields": {"username": "john123", "password": "123456"}}]).encode()
        req_map['create_user'] = urllib.request.Request(self.user_api, data)

        # 创建用户
        with urllib.request.urlopen(req_map['create_user']) as resp:
            print('----Create New User----')
            print(resp.geturl())
            print(resp.getcode(), resp.msg)
            print(resp.info())
            body = resp.read()
            print(body.decode())
            print('----Create User Ended----')
            pk = json.loads(body.decode()).get('id')
            req_map['del'] = urllib.request.Request(self.user_api+str(pk), method='DELETE')

        # 登陆
        data = json.dumps({'username': 'john123', 'password': '123456'}).encode()
        req_map['login'] = urllib.request.Request(self.login_api, data)
        with urllib.request.urlopen(req_map['login']) as resp:
            print('----Login Test----')
            print(resp.geturl())
            print(resp.getcode(), resp.msg)
            print(resp.info())
            print('----Login Test Ended----')

        # 访问 account 列表
        with urllib.request.urlopen(self.account_api) as r:
            print('----Get AccountList Test----')
            print(r.geturl())
            print(r.getcode(), r.msg)
            print(r.info())
            print('----Get AccountList Test Ended----')

        # 登出
        req_map['logout'] = urllib.request.Request(self.logout_api)
        with urllib.request.urlopen(req_map['logout']) as resp:
            print('----Logout Test----')
            print(resp.geturl())
            print(resp.getcode(), resp.msg)
            print(resp.info())
            print('----Logout Test Ended----')

        # 删除新建用户
        with urllib.request.urlopen(req_map['del']) as resp:
            print('----Del User Test----')
            print(resp.geturl())
            print(resp.getcode(), resp.msg)
            print(resp.info())
            print('----Del User Test Ended----')



