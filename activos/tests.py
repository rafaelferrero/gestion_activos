"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        #Tests that 1 + 1 always equals 2.
        self.assertEqual(1 + 1, 2)
"""


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    #return [b"Hello World"] # python3
    return ["Hello World"] # python2