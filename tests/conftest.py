import pytest

from locators import Locators
import urls

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture # фикстура, которая создает драйвер
def driver():
    driver = webdriver.Chrome()
    yield  driver

    driver.quit()

@pytest.fixture() # фикстура производит регистрацию
def registrations(driver):
    driver.get(urls.stellarburgers)
    driver.find_element(*Locators.in_to_account).click()
    # Добавь ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entrance))
    # Выполни вход
    # Найди поле "Email" и заполни его
    driver.find_element(*Locators.input_name).send_keys("khokhlova_14@gmail.ru")
    # Найди поле "Пароль" и заполни его
    driver.find_element(*Locators.input_password).send_keys("Deudeu")
    # Найди кнопку "Войти" и кликни по ней
    driver.find_element(*Locators.login_button).click()
    # Добавь ожидание для загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_burger))
