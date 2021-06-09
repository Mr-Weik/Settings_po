from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):
    # ---------- 元素的特征 ----------
    search_button = By.ID, "com.android.settings:id/search"

    # ---------- 元素的操作 ----------

    def click_search(self):
        self.click(self.search_button)
