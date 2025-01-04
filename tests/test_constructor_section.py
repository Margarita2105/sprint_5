from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Переходы к разделам

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

#Переход к разделу Соусы
#Находим кнопку "Соусы" и нажимаем
driver.find_element(By.XPATH, ".//div[starts-with(@class,'tab_tab__1SPyG')][2]").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".text.text_type_main-large.mb-5.mt-10")))
#После активации раздела Соусы в тег добавляется tab_tab_type_current
#Запоминаем имя второго тега после активации раздела Соусы
tag_two = driver.find_element(By.XPATH, ".//div[starts-with(@class,'tab_tab__1SPyG')][2]").get_attribute("class")
#Проверяем есть ли в теге tab_tab_type_current
assert 'tab_tab_type_current' in tag_two

#Переход к разделу Начинки
#Находим кнопку "Начинки" и нажимаем
driver.find_element(By.XPATH, ".//div[starts-with(@class,'tab_tab__1SPyG')][3]").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".text.text_type_main-large.mb-5.mt-10")))
#Запоминаем имя третьего тега после активации раздела Начинки
tag_three = driver.find_element(By.XPATH, ".//div[starts-with(@class,'tab_tab__1SPyG')][3]").get_attribute("class")
#Проверяем есть ли в теге tab_tab_type_current
assert 'tab_tab_type_current' in tag_three

#Переход к разделу Булки
#Находим кнопку "Булки" и нажимаем
driver.find_element(By.XPATH, ".//div[starts-with(@class,'tab_tab__1SPyG')][1]").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".text.text_type_main-large.mb-5.mt-10")))
#Запоминаем имя первого тега после активации раздела Булки
tag_one = driver.find_element(By.XPATH, ".//div[starts-with(@class,'tab_tab__1SPyG')][1]").get_attribute("class")
#Проверяем есть ли в теге tab_tab_type_current
assert 'tab_tab_type_current' in tag_one

driver.quit()
