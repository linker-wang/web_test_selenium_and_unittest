import unittest

class MyUnit(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        # 全局的setUpClass方法
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls):
        # 全局的tearDownClass方法
        return super().tearDownClass()
    
    def setUp(self):
        # 全局的setUp方法
        return super().setUp()
    
    def tearDown(self):
        # 全局的tearDown方法
        return super().tearDown()