import unittest,time
from report.Common.HTMLTestRunner import HTMLTestRunner
discover=unittest.defaultTestLoader.discover('.',pattern='test*.py')
if __name__ == '__main__':
    dir_path="../Report/"
    now=time.strftime("%Y_%m_%d %H_%M_%S")
    file_name=dir_path+now+"Report.html"
    with open(file_name,'wb') as f:
        HTMLTestRunner(stream=f,title="自动化",description='win7').run(discover)
