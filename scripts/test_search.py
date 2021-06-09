import time
import unittest

from page.search_page import SearchPage
from page.setting_page import SettingPage


class TestSearch():
    def setup(self):
        # 创建对象

        # 导模块
        from appium import webdriver

        # 创建一个字典，包装相应的启动参数
        desired_caps = dict()
        # 需要连接的手机的平台(不限制大小写)
        desired_caps['platformName'] = 'Android'
        # 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
        desired_caps['platformVersion'] = '5.1'
        # 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
        desired_caps['deviceName'] = 'huawei p30'
        # 需要启动的程序的包名
        desired_caps['appPackage'] = 'com.android.settings'
        # 需要启动的程序的界面名
        desired_caps['appActivity'] = '.Settings'

        # 连接appium服务器
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.setting_page = SettingPage(self.driver)
        self.search_page = SearchPage(self.driver)

    def teardown(self):
        time.sleep(10)
        self.driver.quit()

    def test_phone(self):
        self.setting_page.click_search()
        self.search_page.input_search('dslnffs')
        self.search_page.click_back()
