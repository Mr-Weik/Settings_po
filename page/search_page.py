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
