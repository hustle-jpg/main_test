from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_tri():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://store.steampowered.com/")

    # Используем JavaScript, чтобы убедиться, что поле для поиска доступно
    witcher_send = wait.until(EC.presence_of_element_located((By.ID, 'store_nav_search_term')))
    driver.execute_script("arguments[0].scrollIntoView(true);", witcher_send)

    # Дополнительная проверка готовности элемента через JavaScript
    is_visible = driver.execute_script("return arguments[0].offsetParent !== null;", witcher_send)
    if is_visible:
        witcher_send.send_keys('The Witcher')
    else:
        print("Поле для поиска недоступно для ввода")

    # Повторим аналогичную проверку перед кликом
    witcher_poisk = wait.until(EC.presence_of_element_located((By.ID, 'store_search_link')))
    driver.execute_script("arguments[0].scrollIntoView(true);", witcher_poisk)

    # Проверяем доступность элемента и кликаем, если он доступен
    is_clickable = driver.execute_script("return arguments[0].offsetParent !== null;", witcher_poisk)
    if is_clickable:
        witcher_poisk.click()
    else:
        print("Кнопка поиска недоступна для клика")

    time.sleep(5)  # Для просмотра результата перед закрытием
    driver.quit()

