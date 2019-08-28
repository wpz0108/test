from appium import webdriver
def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4'
    desired_caps['deviceName'] = '192.168.230.101:5555'
    # APP信息
    # desired_caps['appPackage'] = 'com.android.settings'
    # desired_caps['appActivity'] = '.Settings'
    desired_caps['appPackage'] = 'com.android.mms'
    desired_caps['appActivity'] = '.ui.ConversationList'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver