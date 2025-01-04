from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Вход по кнопке «Войти в аккаунт» на главной

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
#Находим кнопку "Войти в аккаунт" и нажимаем
driver.find_element(By.XPATH, ".//main//button[text()='Войти в аккаунт']").click()
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
#Проверить, что вход выполнен и произошло перенаправление на главную страницу
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quit()

#Вход через кнопку «Личный кабинет»

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
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
#Проверить, что вход выполнен и произошло перенаправление на главную страницу
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quit()

#Вход через кнопку в форме регистрации

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#Переходим к форме регистрации
#Находим кнопку "Войти в аккаунт" и нажимаем
driver.find_element(By.XPATH, ".//main//button[text()='Войти в аккаунт']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
#Находим кнопку "Зарегистрироваться" и нажимаем
driver.find_element(By.CSS_SELECTOR, ".Auth_link__1fOlj[href='/register']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__container")))

#Переходим к форме входа
#Находим кнопку "Войти" и нажимаем
driver.find_element(By.CSS_SELECTOR, ".Auth_link__1fOlj[href='/login']").click()
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
#Проверить, что вход выполнен и произошло перенаправление на главную страницу
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quit()

#Вход через кнопку в форме восстановления пароля

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
#Находим кнопку "Войти в аккаунт" и нажимаем
driver.find_element(By.XPATH, ".//main//button[text()='Войти в аккаунт']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))
#Находим кнопку Восстановить пароль и нажимае
driver.find_element(By.CSS_SELECTOR, ".Auth_link__1fOlj[href='/forgot-password']").click()
# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.CSS_SELECTOR, ".Auth_link__1fOlj[href='/login']").click()
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
#Проверить, что вход выполнен и произошло перенаправление на главную страницу
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

driver.quit()
