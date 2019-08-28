from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class NetworkPage(BaseAction):
    # 不写的话 中间有逗号 相当于元组()
    more_button = By.XPATH,"text,More" # "//*[contains(@text,'More')]"
    networks_button = By.XPATH,"text,bile net" # "//*[contains(@text,'bile net')]"
    net_type_button= By.XPATH,"text,type"  # "//*[contains(@text,'type')]"
    click_2g_button= By.XPATH,"text,2G"  # "//*[contains(@text,'2G')]"
    click_3g_button= By.XPATH,"text,3G"  # "//*[contains(@text,'3G')]"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        self.click_more()
        self.click_networks()
        self.click_net_type()

    def click_more(self):
        self.click(self.more_button)
    def click_networks(self):
        self.click(self.networks_button)
    def click_net_type(self):
        self.click(self.net_type_button)
    def click_2g(self):
        self.click(self.click_2g_button)
    def click_3g(self):
        self.click(self.click_3g_button)