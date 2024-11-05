from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def find_element_with_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_element_with_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_element_with_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def open(self, url):
        self.driver.get(url)