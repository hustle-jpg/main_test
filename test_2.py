from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def test_dva():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://store.steampowered.com/")

    values_in_search = wait.until(EC.presence_of_element_located((By.ID, 'store_nav_search_term')))
    values_in_search.send_keys('The Witcher')

    find_game = wait.until(EC.element_to_be_clickable((By.ID, 'store_search_link')))
    driver.execute_script("arguments[0].click();", find_game)

    click_sort = wait.until(EC.presence_of_element_located((By.ID, 'sort_by_trigger')))
    click_sort.click()

    desc_button = wait.until(EC.presence_of_element_located((By.ID, "Price_ASC")))
    desc_button.click()

    games = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.search_result_row')))

    # # Подсчитываем количество найденных игр
    # actual_game_count = len(games)
    # expected_game_count = 109
    #
    # assert actual_game_count == expected_game_count, f"Ожидалось {expected_game_count} игр, но найдено {actual_game_count}."
