import unittest
from selenium import webdriver
from Common.get_db import MyDBHandler
class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = MyDBHandler()

    def tearDown(self):
        self.db.close()

    def testD(self):
        # 获取投资之后的金额

        sql = 'SELECT * FROM `crm_resource_search` where id =%s;'
        resource = self.db.query(sql, args=[500])
        # resource = self.db.query(sql)
        print(resource['phone_number'])