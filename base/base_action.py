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
