from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class BaseAction():
    def __init__(self,driver):
        self.driver=driver
    def click(self,loc):
        self.find_elem(loc).click()
    def send_keys(self,loc,text):
        self.find_elem(loc).send_keys(text)
    def find_elem(self,loc):
        by=loc[0]
        value=loc[1]
        if by==By.XPATH:
            value=self.make_xpath_feature(value)
        return WebDriverWait(self.driver,10,1).until(lambda x:x.find_element(by,value))
    def find_elems(self,loc):
        by=loc[0]
        value=loc[1]
        if by==By.XPATH:
            value=self.make_xpath_feature(value)
        return WebDriverWait(self.driver,10,1).until(lambda x:x.find_elements(by,value))
    def make_xpath_feature(self,loc):
        start = "//*["
        end = "]"
        feature = ""
        if isinstance(loc,str):
            feature = self.make_xpath_unit_feature(loc)
        elif isinstance(loc,list):
            for i in loc:
                feature+=self.make_xpath_unit_feature(i)+" and "
            feature=feature.rstrip(" and ")
        return start+feature+end

        # //*[contains(@text,'设')]  'text,s'
        # //*[@text='设' and contains(@text,'置')]   ['text,s','text,'z']
        # "text,设置" 包含
        # "text,设置,0" 包含
        # "text,设置,1" 精准
        # ["text,设置" ,"text,设置,1"]
    def make_xpath_unit_feature(self,loc):
        key = 0
        value = 1
        option = 2
        feature = ""
        args=loc.split(',')
        if len(args) == 2:
            feature = "contains(@" + args[key] + ",'" + args[value] + "')"
        elif len(args) == 3:
            if args[option] == '0':
                feature = "contains(@" + args[key] + ",'" + args[value] + "')"
            elif args[option] == '1':
                feature = "@" + args[key] + "='" + args[value] + "'"
        return feature

# 测试字符串函数 注释掉init方法 右键运行
# if __name__ == '__main__':
#     print(BaseAction().make_xpath_feature(['test,a,1','test1,b,0','test2,c']))