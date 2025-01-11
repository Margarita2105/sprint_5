from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
import urls

#Переходы к разделам
class TestConstructor:

    def test_sections_sauces(self, driver):

        driver.get(urls.stellarburgers)
    #Переход к разделу Соусы
        #Находим кнопку "Соусы" и нажимаем
        driver.find_element(*Locators.sauces).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.section_sauces))
        #После активации раздела Соусы в тег добавляется tab_tab_type_current
        #Запоминаем имя второго тега после активации раздела Соусы
        tag_two = driver.find_element(*Locators.sauces).get_attribute("class")
        #Проверяем есть ли в теге tab_tab_type_current
        assert 'tab_tab_type_current' in tag_two

    def test_sections_toppings(self, driver):

        driver.get(urls.stellarburgers)
    #Переход к разделу Начинки
        #Находим кнопку "Начинки" и нажимаем
        driver.find_element(*Locators.toppings).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.section_toppings))
        #Запоминаем имя третьего тега после активации раздела Начинки
        tag_three = driver.find_element(*Locators.toppings).get_attribute("class")
        #Проверяем есть ли в теге tab_tab_type_current
        assert 'tab_tab_type_current' in tag_three

    def test_sections_rolls(self, driver):

        driver.get(urls.stellarburgers)
        driver.find_element(*Locators.toppings).click()
    # Переход к разделу Булки
        # Находим кнопку "Булки" и нажимаем
        driver.find_element(*Locators.rolls).click()
        # Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.section_rolls))
        #Запоминаем имя первого тега после активации раздела Булки
        tag_one = driver.find_element(*Locators.rolls).get_attribute("class")
        #Проверяем есть ли в теге tab_tab_type_current
        assert 'tab_tab_type_current' in tag_one
