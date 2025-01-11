
from selenium.webdriver.common.by import By

class Locators:
#кнопка "Войти в аккаунт" на главной странице
    in_to_account = (By.XPATH, ".//main//button[text()='Войти в аккаунт']")
#кнопка Вход на странице Войти в аккаунт
    entrance = (By.XPATH, ".//h2[text()='Вход']")
#кнопка "Зарегистрироваться" в личном кабинете
    registration = (By.CSS_SELECTOR, ".Auth_link__1fOlj[href='/register']")
#картинки на главной странице
    picture = (By.CLASS_NAME, "input__container")
#поле Имя в форме регистрации
    field_name = (By.XPATH, "//main//label[text()='Имя']/parent::*/input")
#поле Email в форме регистрации
    field_email = (By.XPATH, "//main//label[text()='Email']/parent::*/input")
#поле Пароль в форме регистрации
    field_password = (By.XPATH, "//main//input[@type='password']")
#кнопка Зарегистрироваться в форме регистрации
    register = (By.XPATH, ".//main//button[text()='Зарегистрироваться']")
#надпись Некорректный пароль
    incorrect = (By.XPATH, "//main//p[@class='input__error text_type_main-default']")
#поле "Email" на странице Войти в аккаунт
    input_name = (By.XPATH, ".//input[@name='name']")
#поле "Пароль" на странице Войти в аккаунт
    input_password = (By.XPATH, ".//input[@name='Пароль']")
#кнопка Войти на странице Войти в аккаунт
    login_button = (By.XPATH, ".//button[text()='Войти']")
#надпись Собери бургер
    assemble_burger = (By.CSS_SELECTOR, ".text.text_type_main-large.mb-5.mt-10")
#кнопка Оформить заказ на главной странице для зарегистрированного пользователя
    place_order = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
#кнопка Профиль в личном кабинете
    account_link = (By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")
#кнопка Выход для выхода из аккуанта
    exit_button = (By.XPATH, ".//button[text()='Выход']")
#кнопка "Личный кабинет"
    personal_account = (By.XPATH, ".//p[text()='Личный Кабинет']")
#кнопка Войти в форме регистрации
    login_button_in_login_form = (By.CSS_SELECTOR, ".Auth_link__1fOlj[href='/login']")
#кнопка Восстановить пароль
    recover_password = (By.CSS_SELECTOR, ".Auth_link__1fOlj[href='/forgot-password']")
#кнопка "Войти" на странице входа после нажатия на Восстановить пароль
    log_in_after_password_recovery = (By.CSS_SELECTOR, ".Auth_link__1fOlj[href='/login']")
#надпись Конструктор на главной странице
    designer = (By.XPATH, ".//p[text()='Конструктор']")
#логотип
    logo = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")
#кнопка Булки в шапке конструктора
    rolls = (By.XPATH, ".//span[text()='Булки']/parent::*")
#кнопка Соусы в шапке конструктора
    sauces = (By.XPATH, ".//span[text()='Соусы']/parent::*")
#кнопка Начинки в шапке конструктора
    toppings = (By.XPATH, ".//span[text()='Начинки']/parent::*")
#надпись Соусы в конструкторе
    section_sauces = (By.XPATH, ".//h2[text()='Соусы']")
#надпись Начинки в конструкторе
    section_toppings = (By.XPATH, ".//h2[text()='Начинки']")
#надпись Булки в конструкторе
    section_rolls = (By.XPATH, ".//h2[text()='Булки']")
