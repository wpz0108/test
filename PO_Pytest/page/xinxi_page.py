from selenium.webdriver.common.by import By
from base.base_action import BaseAction
class XinXi(BaseAction):
    search_button=By.XPATH,"resource-id,id/search"
    input_button=By.XPATH,"text,messaging"
    back_button=By.XPATH,"resource-id,up"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
    def click_search(self):
        self.click(self.search_button)
    def input_search(self,content):
        self.send_keys(self.input_button,content)
    def click_back(self):
        self.click(self.back_button)