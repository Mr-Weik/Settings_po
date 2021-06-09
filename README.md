+ 上传 Android端的Setting模板

+ 采用Po模式进行编写

  + 分别为 `Base`  `Page`  `Scripts` `pytest.ini` 组成

+ Base

  + 放置公共方法

  + ```python
    from selenium.webdriver.support.wait import WebDriverWait
    
    
    class BaseAction:
    
        def __init__(self, driver):
            self.driver = driver
    
        def find_element(self, feature, timeout=10, poll=1):
            return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))
    
        def click(self, feature, timeout=10, poll=1):
            self.find_element(feature, timeout, poll).click()
    
        def input(self, feature, text, timeout=10, poll=1):
            self.find_element(feature, timeout, poll).send_keys(text)
    
        def clear_and_input(self, feature, text, timeout=10, poll=1):
            self.clear(feature, timeout, poll)
            self.find_element(feature, timeout, poll).send_keys(text)
    
        def clear(self, feature, timeout=10, poll=1):
            self.find_element(feature, timeout, poll).clear()
    
        def get_text(self, feature, timeout=10, poll=1):
            return self.find_element(feature, timeout, poll).text
    
    ```

  + 

+ Page

  + 放置单页面的元素获取以及动作

  + **search_page页面**

    ```python
    from selenium.webdriver.common.by import By
    
    from base.base_action import BaseAction
    
    
    class SearchPage(BaseAction):
        # 确定元素特征
        search_input = By.ID, 'android:id/search_src_text'
    
        search_back = By.XPATH, "//*[@content-desc='收起']"
    
        # 确定元素动作
    
        def input_search(self, text):
            self.input(self.search_input, text)
    
        def click_back(self):
            self.click(self.search_back)
    
    ```

  + **setting_page页面**

  + ```python
    from selenium.webdriver.common.by import By
    
    from base.base_action import BaseAction
    
    
    class SettingPage(BaseAction):
        # ---------- 元素的特征 ----------
        search_button = By.ID, "com.android.settings:id/search"
    
        # ---------- 元素的操作 ----------
    
        def click_search(self):
            self.click(self.search_button)
    
    ```

  + 

+ scripts

  + 放置采用的ui动作

  + ```python
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
    
    ```

+ `pytest.ini`放置的为配置文件

  + ```
    [pytest]
    addopts = -s  --html=report/report.html  -p no:warnings
    testpaths = ./scripts
    python_files = test_*.py
    python_classes = Test*
    python_functions = test_*

+ 附上结构图
+ [![267li4.png](https://z3.ax1x.com/2021/06/09/267li4.png)](https://imgtu.com/i/267li4)

