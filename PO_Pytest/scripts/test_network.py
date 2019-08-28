import os,sys
sys.path.append(os.getcwd())
# from base.xx base模块是自定义的 引用时找不到路径 要将当前项目目录添加到系统路径中
from base.base_driver import init_driver
from page.network_page import NetworkPage
class TestNetwork():
    def setup(self):
        self.driver=init_driver()
        self.network_page=NetworkPage(self.driver)
    def test_2g(self):
        # 可以将相同的动作放到对应page的init中
        # self.network_page.click_more()
        # self.network_page.click_networks()
        # self.network_page.click_net_type()
        self.network_page.click_2g()
    def test_3g(self):
        # self.network_page.click_more()
        # self.network_page.click_networks()
        # self.network_page.click_net_type()
        self.network_page.click_3g()