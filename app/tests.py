from django.test import TestCase

# Create your tests here.
import http.cookiejar, urllib.request


class UserTest(TestCase):
    user_api = 'http://localhost:8000/api/user/'
    login_api = 'http://localhost:8000/api/login/'
    logout_api = 'http://localhost:8000/api/logout/'
    account_api = 'http://localhost:8000/api/account/'

    def test_001(self):
        session_api = 'http://localhost:8000/api/session/'
        data = '{"username": "zgwldrc@163.com", "password": "xiayu123"}'

        http = Http()
        http.post(session_api, data.encode())
        http.delete(session_api)

    def test_002(self):
        session_api = 'http://localhost:8000/api/session/'
        data = '{"username": "zgwldrc@163.com", "password": "xiayu1234"}'

        http = Http()
        try:

            http.post(session_api, data.encode())
        except HTTPError:



class Http:
    def __init__(self, cookiejar=True):
        handlers = []
        if cookiejar:
            cookiejar = http.cookiejar.CookieJar()
            cookieprocessor = urllib.request.HTTPCookieProcessor(cookiejar)
            handlers.append(cookieprocessor)
        self.opener = urllib.request.build_opener(*handlers)
        urllib.request.install_opener(self.opener)

    def open(self, request):
        with urllib.request.urlopen(request) as r:
            print('请求方法: {},请求URL: {}'.format(request.get_method(), r.geturl()))
            print('响应状态码: {}, 消息: {}'.format(r.getcode(), r.msg))
            print(r.info())
            print(r.read().decode())

    def post(self, url, data, options={}):
        req = urllib.request.Request(url, data)
        self.open(req)

    def delete(self, url, options={}):
        req = urllib.request.Request(url, method='DELETE')
        self.open(req)







