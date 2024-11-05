import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


@pytest.mark.parametrize("game_name", ["The Witcher", "Fallout"])
def test_search_game(driver, game_name):
    home_page = HomePage(driver)
    search_results_page = SearchResultsPage(driver)

    home_page.open("https://store.steampowered.com/")

    home_page.search_game(game_name)

    assert "search" in driver.current_url

    search_results_page.apply_filter("По убыванию цены")

    # game_list = search_results_page.get_game_list()
    # assert len(game_list) >= 10
