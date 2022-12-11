from django.test import TestCase
from .func import *
import json
# Create your tests here.

class TestAddConf (TestCase):
    def test(self):
        a = addConf("1", "2", "5")
        a.pop("id")
        self.assertEqual(a, {'Title': "1", 'ConfDate': "2", 'ConfTag': "5"})
class TestAddConf1 (TestCase):
    def test(self):
        a = addConf("test", "test", "test")
        a.pop("id")
        self.assertEqual(a, {'Title': "test", 'ConfDate': "test", 'ConfTag': "test"})

class TestGetConf (TestCase):
    def test(self):
        a = getConf("Название", "25.10.22", "работа")
        self.assertEqual(a[0], {'id': 65, 'Title': "Название", 'ConfDate': "25.10.22", 'ConfTag': "работа"})
class TestGetConf1 (TestCase):
    def test(self):
        a = getConf("qwert", "qwert", "qwert")
        self.assertEqual(a[0], {'id': 92, 'Title': "qwert", 'ConfDate': "qwert", 'ConfTag': "qwert"})
class TestGetConf2 (TestCase):
    def test(self):
        a = getConf("qwert", "qwert", "qwert")
        self.assertEqual(a[0], {'id': 92, 'Title': "qwert", 'ConfDate': "qwert", 'ConfTag': "qwert"})
