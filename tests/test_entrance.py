from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators
import urls

class TestEntrance:
# Вход по кнопке «Войти в аккаунт» на главной
    def test_log_in_to_account_button(self, driver):

        driver.get(urls.stellarburgers)
#Находим кнопку "Войти в аккаунт" и нажимаем
        driver.find_element(*Locators.in_to_account).click()
# Добавь ожидание для загрузки страницы
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(Locators.entrance))
# Выполни вход
# Найди поле "Email" и заполни его
        driver.find_element(*Locators.input_name).send_keys("khokhlova_14@gmail.ru")
# Найди поле "Пароль" и заполни его
        driver.find_element(*Locators.input_password).send_keys("Deudeu")
# Найди кнопку "Войти" и кликни по ней
        driver.find_element(*Locators.login_button).click()
# Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(Locators.assemble_burger))
#Проверить, что вход выполнен и произошло перенаправление на главную страницу
        assert driver.find_element(*Locators.place_order).text == 'Оформить заказ'

#Вход через кнопку «Личный кабинет»

    def test_log_in_personal_account_button(self, driver):

        driver.get(urls.stellarburgers)
#Находим кнопку "Личный кабинет" и нажимаем
        driver.find_element(*Locators.personal_account).click()
# Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entrance))
# Выполни вход
# Найди поле "Email" и заполни его
        driver.find_element(*Locators.input_name).send_keys("khokhlova_14@gmail.ru")
# Найди поле "Пароль" и заполни его
        driver.find_element(*Locators.input_password).send_keys("Deudeu")
# Найди кнопку "Войти" и кликни по ней
        driver.find_element(*Locators.login_button).click()
# Добавь явное ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.assemble_burger))
#Проверить, что вход выполнен и произошло перенаправление на главную страницу
        assert driver.find_element(*Locators.place_order).text == 'Оформить заказ'

#Вход через кнопку в форме регистрации

    def test_log_in_button_in_registration_form(self, driver):

        driver.get(urls.stellarburgers)
#Переходим к форме регистрации
#Находим кнопку "Войти в аккаунт" и нажимаем
        driver.find_element(*Locators.in_to_account).click()
# Добавь ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entrance))
#Находим кнопку "Зарегистрироваться" и нажимаем
        driver.find_element(*Locators.registration).click()
# Добавь ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.picture))
#Переходим к форме входа
#Находим кнопку "Войти" и нажимаем
        driver.find_element(*Locators.login_button_in_login_form).click()
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
#Проверить, что вход выполнен и произошло перенаправление на главную страницу
        assert driver.find_element(*Locators.place_order).text == 'Оформить заказ'

#Вход через кнопку в форме восстановления пароля

    def test_login_button_in_password_recovere_form(self, driver):

        driver.get(urls.stellarburgers)
#Находим кнопку "Войти в аккаунт" и нажимаем
        driver.find_element(*Locators.in_to_account).click()
# Добавь ожидание для загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.entrance))
#Находим кнопку Восстановить пароль и нажимае
        driver.find_element(*Locators.recover_password).click()
# Найди кнопку "Войти" и кликни по ней
        driver.find_element(*Locators.log_in_after_password_recovery).click()
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
#Проверить, что вход выполнен и произошло перенаправление на главную страницу
        assert driver.find_element(*Locators.place_order).text == 'Оформить заказ'
