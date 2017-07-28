from django.test import TestCase

# Create your tests here.
from urllib.request import urlopen, Request
import json

class UserTest(TestCase):
    api = 'http://localhost:8000/api/user/'

    def test_create_delete_user(self):

        d = [
              {
                "model": "auth.user",
                "fields": {
                  "username": "john123",
                  "password": "123456"
                }
              }
            ]

        with urlopen(self.api, json.dumps(d).encode()) as resp:
            print(resp.getcode(), resp.msg)
            data = resp.read().decode()
            print(data)
            pk = json.loads(data)['id']
            del_req = Request(self.api+str(pk), method='DELETE')
            with urlopen(del_req) as resp2:
                print(resp2.getcode(), resp2.msg)

    def test_login_logout(self):
        login_api = 'http://localhost:8000/api/login'
        logout_api = 'http://localhost:8000/api/logout'
        login_req = Request(
            login_api,
            json.dumps({
                'username': 'xiayu',
                'password': 'xiayu123'
            }).encode(),
            method='POST'
        )





