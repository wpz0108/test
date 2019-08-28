import os,sys
import pytest
import allure
sys.path.append(os.getcwd())
from base.base_driver import init_driver
from page.xinxi_page import XinXi
from base.base_yml import yml_data_file

def data_with_key(key):
    """
    传入测试方法名 可获取对该测试方法准备的数据
    :param key: 测试方法名
    :return: 列表 测试数据
    """
    if key=="test_search":
        data=yml_data_file('xinxi_data')['test_search']
        i=0
        ln=len(data)
        while i<ln:
            data[i]=data[i]+'houzhui'
            i+=1
        return data
    else:
        return yml_data_file('xinxi_data')[key]

class TestXinxi():
    def setup(self):
        self.driver=init_driver()
        self.xinxi_page=XinXi(self.driver)

    @allure.step(title="测试搜索")
    @pytest.mark.parametrize('key', data_with_key("test_search"))
    def test_search(self,key):
        allure.attach("点击搜索按钮")
        self.xinxi_page.click_search()
        allure.attach("输入数据")
        self.xinxi_page.input_search(key)
        allure.attach("点击返回")
        self.xinxi_page.click_back()
    @pytest.mark.parametrize('key', data_with_key("test_search1"))
    def test_search1(self,key):
        self.xinxi_page.click_search()
        self.xinxi_page.input_search(key)
        self.xinxi_page.click_back()
