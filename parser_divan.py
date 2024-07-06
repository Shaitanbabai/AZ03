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
prices = driver.find_elements(By.XPATH, '//span[@data-testid="price"]')

# Парсим и выводим цены
# for price in prices:
#     print(price.text)

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()


def clean_price(pure_price):
    # Удаляем "₽/мес." и преобразуем в число
    return int(pure_price.replace(' ₽/мес.', '', 'руб.').replace(' ', ''))


# Чтение данных из исходного CSV файла и их обработка
input_file = 'prices.csv'
output_file = 'pure_prices.csv'

with (open(input_file, mode='r', encoding='utf-8') as infile,
      open(output_file, mode='w', newline='', encoding='utf-8') as outfile):
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        clean_row = [clean_price(row[0])]
        writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")
