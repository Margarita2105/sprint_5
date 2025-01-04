from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
#Находим кнопку "Войти в аккаунт" и нажимаем
driver.find_element(By.XPATH, ".//main//button[text()='Войти в аккаунт']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
#Находим кнопку "Зарегистрироваться" и нажимаем
driver.find_element(By.CSS_SELECTOR, ".Auth_link__1fOlj[href='/register']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__container")))
# Выполни регистрацию
# Найди поле "Имя" и заполни его
driver.find_element(By.XPATH, "//main//label[text()='Имя']/parent::*/input").send_keys("Моеимя")
# Найди поле "Email" и заполни его
driver.find_element(By.XPATH, "//main//label[text()='Email']/parent::*/input").send_keys("khokhlova_14@gmail.com")
# Найди поле "Пароль" и заполни его
driver.find_element(By.XPATH, "//main//input[@type='password']").send_keys("Deusex77.")
# Найди кнопку "Зарегистрироваться" и кликни по ней
driver.find_element(By.XPATH, ".//main//button[text()='Зарегистрироваться']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
#Проверить, что регистрация пройдена и произошло перенаправление на страницу входа
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()
#Проверить ошибку заполнения поля Пароль

driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")
#Находим кнопку "Войти в аккаунт" и нажимаем
driver.find_element(By.XPATH, ".//main//button[text()='Войти в аккаунт']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
#Находим кнопку "Зарегистрироваться" и нажимаем
driver.find_element(By.CSS_SELECTOR, ".Auth_link__1fOlj[href='/register']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__container")))
# Выполни регистрацию
# Найди поле "Имя" и заполни его
driver.find_element(By.XPATH, "//main//label[text()='Имя']/parent::*/input").send_keys("Моеимя")
# Найди поле "Email" и заполни его
driver.find_element(By.XPATH, "//main//label[text()='Email']/parent::*/input").send_keys("khokhlova_14@gmail.com")
# Найди поле "Пароль" и заполни его некорректным значением из 4 символов
driver.find_element(By.XPATH, "//main//input[@type='password']").send_keys("Deus")
# Найди кнопку "Зарегистрироваться" и кликни по ней
driver.find_element(By.XPATH, ".//main//button[text()='Зарегистрироваться']").click()
#Проверить текст появившейся ошибки
assert driver.find_element(By.XPATH, "//main//p[@class='input__error text_type_main-default']").text == 'Некорректный пароль'

driver.quit()
