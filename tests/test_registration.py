import random

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

from locators import Locators
import urls

class TestRegistration:

    def test_successful_registration(self, driver):

        driver.get(urls.stellarburgers)
    #Находим кнопку "Войти в аккаунт" и нажимаем
        driver.find_element(*Locators.in_to_account).click()
    # Добавь ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entrance))
    #Находим кнопку "Зарегистрироваться" и нажимаем
        driver.find_element(*Locators.registration).click()
    # Добавь ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.picture))
    # Выполни регистрацию
        # Найди поле "Имя" и заполни его
        driver.find_element(*Locators.field_name).send_keys("Моеимя")
        email = str(random.randint(1, 999))+'@gmail.com'
        # Найди поле "Email" и заполни его
        driver.find_element(*Locators.field_email).send_keys(email)
        # Найди поле "Пароль" и заполни его
        driver.find_element(*Locators.field_password).send_keys("Deudeu")
        # Найди кнопку "Зарегистрироваться" и кликни по ней
        driver.find_element(*Locators.register).click()
    # Добавь ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entrance))
    #Проверить, что регистрация пройдена и произошло перенаправление на страницу входа
        assert driver.current_url == urls.stellarburgers+'login'
        #driver.quit()
#Проверить ошибку заполнения поля Пароль

    def test_registering_incorrect_password(self, driver):

        driver.get(urls.stellarburgers)
    #Находим кнопку "Войти в аккаунт" и нажимаем
        driver.find_element(*Locators.in_to_account).click()
    # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entrance))
    #Находим кнопку "Зарегистрироваться" и нажимаем
        driver.find_element(*Locators.registration).click()
    # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.picture))
    # Выполни регистрацию
        # Найди поле "Имя" и заполни его
        driver.find_element(*Locators.field_name).send_keys("Моеимя")
        email = str(random.randint(1, 999))+'@gmail.com'
        # Найди поле "Email" и заполни его
        driver.find_element(*Locators.field_email).send_keys(email)
        # Найди поле "Пароль" и заполни его некорректным значением из 4 символов
        driver.find_element(*Locators.field_password).send_keys("Deus")
        # Найди кнопку "Зарегистрироваться" и кликни по ней
        driver.find_element(*Locators.register).click()
    #Проверить текст появившейся ошибки
        assert driver.find_element(*Locators.incorrect).text == 'Некорректный пароль'
