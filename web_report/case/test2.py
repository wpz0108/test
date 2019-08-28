import unittest
import time
import sys
from selenium import webdriver

class Test02(unittest.TestCase):
    def setUp(self):
        print('test2 up')
    def tearDown(self):
        print('test2 down')
    def test001(self):
        self.driver = webdriver.Firefox()
        self.driver.get(r"file:///d:/test/index.html")
        try:
            self.assertIn('admin', 'add')
        except AssertionError:
            print('test002 zhixing')
            nowtime = time.strftime('%Y_%m_%d %H_%M_%S')
            # 动态保存异常的截图 时间--错误信息
            self.driver.get_screenshot_as_file("./img/%s--%s.png" % (nowtime, sys.exc_info()[1]))
            raise
    def test003(self):
        print("test002 xxx")
if __name__=="__main__":
    unittest.main()
