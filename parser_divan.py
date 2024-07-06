from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
import time
import csv
# import pandas as pd
# import matplotlib.pyplot as plt

driver = webdriver.Chrome()

url = 'https://www.divan.ru/ekaterinburg/category/pramye-divany'
# Открытие страницы
driver.get(url)
time.sleep(5)

# Получаем элементы с ценами
prices = driver.find_elements(By.XPATH, '//span[@class="price__main-value"]')

# Парсим и выводим цены
for price in prices:
    print(price.text)

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()
