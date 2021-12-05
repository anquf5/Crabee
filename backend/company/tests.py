from unittest import mock
from unittest.mock import patch

from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import force_authenticate
from django.shortcuts import reverse
# Create your tests here.
import unittest
from django.test import Client
from crabee_project import settings


class APITest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.client = Client()


    # def test_company_list(self):
    #     print("Test API: /api/company/ ")
    #     response = self.client.get("/api/company/")
    #     content = response.json()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(content),21)
    #
    # def test_index_list(self):
    #     print("Test API: /api/index_company/ ")
    #     response = self.client.get("/api/index_company/")
    #     content = response.json()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(content), 6)
    #
    # def test_company_detail(self):
    #     print("Test API: /api/company/1/ ")
    #     print("Test company detail")
    #     response = self.client.get("/api/company/1/")
    #     content = response.json()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(content['id'],1)
    #
    #     print("Test other companies")
    #     response = self.client.post("/api/company/", data={'company_id':1})
    #     contents = response.json()
    #     self.assertEqual(response.status_code,200)
    #     for content in contents:
    #         self.assertNotEqual(content['id'],1)
    #
    # def log_in_an_account(self):
    #     # username: user01 password:aaabbbccc111
    #     self.client.post("/api/token/login", data={"username":"admin", "password":"admin"})

    def test_company_add_review(self):
        print("Test API: /api/company_review/add ")

        @mock.patch('django.contrib.auth.middleware.get_user')
        def run_step(mock_random):
            mock_random.return_value = User.objects.first()

        run_step()

        header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
                  "Accept": "application/json, text/plain, */*",
                  "Authorization": "Token 658492072e7781285f6ea62b332c4ec36de0b9cf",
                  "Content-Type": "application/json",
                  "Origin": "http://127.0.0.1:8080",
                  "Referer": "http://127.0.0.1:8080/",
                  "Sec-Fetch-Dest": "empty",
                  "Sec-Fetch-Mode": "cors",
                  "Sec-Fetch-Site": "cross-site",
                  "sessionid": "l33jsqqujs2sb1jfc7ehuwjla27tlsj8",
                  "csrftoken": "yLApAns1R4uXamrrjqXTme6hoXcf1LMX5f7EoURX1O3qnjR38SOdCkQuCiFtpYoo",
                  "crossDomain": True
                  }
        # Add review with user login and all parameters full.

        params1 = {"cid": "1",
                   "job": "Java Developer",
                   "title": "A good experience",
                   "content": "AAA",
                   "rate": 5,
                   "difficulty": 'Easy',
                   }
        url = reverse('company:add_review')
        response = self.client.post(url, data=params1, header=header)

        self.assertEqual(response.status_code, 200)

        #POST. Add review with user login and lack of ‘rate’ parameter.
        params2 = {"cid": "2",
                   "job": "Java Developer",
                   "title": "A good experience",
                   "content": "AAA",
                   "difficulty": 'Easy',
                   }
        response = self.client.post("/api/company_review/add/", data=params2, headers=header)
        content = response.json()
        self.assertEqual(content['msg'], 1)

        # POST. Add review with user login and lack of ‘interview difficulty’ parameter.
        params1 = {"cid": "1",
                   "job": "Java Developer",
                   "title": "A good experience",
                   "content": "AAA",
                   "rate": 5,
                   }
        response = self.client.post("/api/company_review/add/", data=params1, headers=header)
        content = response.json()
        self.assertEqual(content['msg'], 1)

        # POST. Add review with user login and lack of ‘title’ parameter.
        params1 = {
                   "cid": "1",
                   "job": "Java Developer",
                   "content": "AAA",
                   "difficulty": 'Easy',
                   }
        response = self.client.post("/api/company_review/add/", data=params1, headers=header)
        content = response.json()
        self.assertEqual(content['msg'], 1)

        # POST. Add review with user login and lack of ‘content’ parameter..
        params1 = {
            "cid": "1",
            "job": "Java Developer",
            "difficulty": 'Easy',
            "title": "A good experience",
        }
        response = self.client.post("/api/company_review/add/", data=params1, headers=header)
        content = response.json()
        self.assertEqual(content['msg'], 1)

    def test_company_search(self):
        print("Test API: /api/company/search ")
        query = {"query":"Amazon"}
        response = self.client.post("/api/company/search/", query)
        content = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content[0]['id'], 1)

    def test_discussion_topic(self):
        print("Test API: /api/topic ")
        response = self.client.get("/api/topic/")
        self.assertEqual(response.status_code, 200)

    def test_topic_add(self):
        print("Test API: /api/topic/add ")
        # Add review with user login and all parameters full.
        params1 = {"title":"aaa",
                   "content":"aaa"
                   }
        response = self.client.post("/api/topic/add/", data=params1)
        self.assertEqual(response.status_code, 200)

    def test_topic_detail(self):
        print("Test API: /api/topic/1 ")
        response = self.client.get("/api/topic/1/")
        content = response.json()
        self.assertEqual(response.status_code, 200)

    def test_topic_reply(self):
        print("Test API: /api/topic/add ")
        # Add review with user login and all parameters full.
        params1 = {'tid': 1,
                   'content': 'aaa'
                   }
        response = self.client.post("/api/topic/reply/", data=params1)
        self.assertEqual(response.status_code, 200)
