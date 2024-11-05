from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "'store_nav_search_term'")
    SEARCH_BUTTON = (By.ID, "search-button")

    def search_game(self, game_name):
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.send_keys(game_name)
        search_button = self.find_element(self.SEARCH_BUTTON)
        search_button.click()
