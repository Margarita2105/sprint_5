from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
import urls

#Переход по клику на «Личный кабинет»
class TestPersonalAccount:

    def test_click_through_to_personal_account(self, driver, registrations):
    #Уже зарегистрированными заходим в Личный кабинет
    #Находим кнопку "Личный кабинет" и нажимаем
        driver.find_element(*Locators.personal_account).click()
    # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.account_link))
    #Проверить, что произошел переход в личный кабинет
        assert driver.current_url == urls.stellarburgers+'account/profile'
