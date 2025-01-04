from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Выход по кнопке «Выйти» в личном кабинете

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#Сначала необходимо зарегистрироваться
#Находим кнопку "Личный кабинет" и нажимаем
driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
# Выполни вход
# Найди поле "Email" и заполни его
driver.find_element(By.XPATH, ".//input[@name='name']").send_keys("khokhlova_14@gmail.com")
# Найди поле "Пароль" и заполни его
driver.find_element(By.XPATH, ".//input[@name='Пароль']").send_keys("Deusex77.")
# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.XPATH, ".//button[text()='Войти']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".text.text_type_main-large.mb-5.mt-10")))

#Уже зарегистрированными заходим в Личный кабинет
#Находим кнопку "Личный кабинет" и нажимаем
driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")))

#Находим кнопку Выход и нажимаем
driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
#Проверить, что произошел переход на форму входа
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()
