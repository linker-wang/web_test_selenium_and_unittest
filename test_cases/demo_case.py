from utils.unit.my_unit import MyUnit
from utils.logging.web_logger import weblog

class DemoCase(MyUnit):
    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_001_demo(self):
        try:
            test_expr= (1 > 3)
            self.assertTrue(test_expr, "表达式错误")
        except Exception as e:
            weblog.error(e)
            raise e