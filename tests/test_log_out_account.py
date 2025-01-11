from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
import urls

#Выход по кнопке «Выйти» в личном кабинете
class TestExit:

    def test_exit_using_exit_button(self, driver, registrations):
#Уже зарегистрированными заходим в Личный кабинет
#Находим кнопку "Личный кабинет" и нажимаем
        driver.find_element(*Locators.personal_account).click()
# Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.account_link))
#Находим кнопку Выход и нажимаем
        driver.find_element(*Locators.exit_button).click()
# Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entrance))
#Проверить, что произошел переход на форму входа
        assert driver.current_url == urls.stellarburgers+'login'
