from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    FILTER_DROPDOWN = (By.ID, "price-filter")
    GAME_LIST = (By.CLASS_NAME, "game-item")

    def apply_filter(self, filter_value):
        dropdown = self.find_element(self.FILTER_DROPDOWN)
        dropdown.select_by_visible_text(filter_value)

    def get_game_list(self):
        return self.driver.find_elements(*self.GAME_LIST)
