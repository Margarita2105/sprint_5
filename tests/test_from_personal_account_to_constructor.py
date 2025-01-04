from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Переход из личного кабинета по клику на «Конструктор»

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

#Находим кнопку Конструктор и нажимаем на неё
driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,".//h1[text()='Соберите бургер']")))
#Проверить, что произошел переход в конструктор
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

driver.quit()

#Переход из личного кабинета по клику на на логотип Stellar Burgers

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

#Находим логотип Stellar Burgers и нажимаем
driver.find_element(By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH,".//h1[text()='Соберите бургер']")))
#Проверить, что произошел переход в конструктор
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

driver.quit()
