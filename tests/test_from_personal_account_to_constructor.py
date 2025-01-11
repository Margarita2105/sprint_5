from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
import urls

class TestTransition:
#Переход из личного кабинета по клику на «Конструктор»
# Вход по кнопке «Войти в аккаунт» на главной
    def test_sign_in_to_account_button(self, driver, registrations):
#Уже зарегистрированными заходим в Личный кабинет
#Находим кнопку "Личный кабинет" и нажимаем
        driver.find_element(*Locators.personal_account).click()
# Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.account_link))
#Находим кнопку Конструктор и нажимаем на неё
        driver.find_element(*Locators.designer).click()
# Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_burger))
#Проверить, что произошел переход в конструктор
        assert driver.current_url == urls.stellarburgers

#Переход из личного кабинета по клику на на логотип Stellar Burgers

    def test_clicking_on_Stellar_Burgers_logo(self, driver, registrations):
#Уже зарегистрированными заходим в Личный кабинет
#Находим кнопку "Личный кабинет" и нажимаем
        driver.find_element(*Locators.personal_account).click()
# Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.account_link))
#Находим логотип Stellar Burgers и нажимаем
        driver.find_element(*Locators.logo).click()
# Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Locators.assemble_burger)))
#Проверить, что произошел переход в конструктор
        assert driver.current_url == urls.stellarburgers
