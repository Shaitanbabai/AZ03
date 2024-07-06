from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

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


def clean_price(pure_price):
    # Удаляем "₽/мес." и преобразуем в число
    return int(pure_price.replace('руб.', '').replace(' ', '').replace('\u2009', ''))


# Чтение данных из исходного CSV файла и их обработка
input_file = 'prices.csv'
output_file = 'pure_prices.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Читаем заголовок и записываем его в новый файл
    header = next(reader)
    writer.writerow(header)

    # Обрабатываем и записываем данные строк
    for row in reader:
        if row:  # Проверка на пустые строки
            clean_row = [clean_price(row[0])]
            writer.writerow(clean_row)

print(f"Обработанные данные сохранены в файл {output_file}")

# Закрытие драйвера
driver.quit()

# Загрузка данных из CSV-файла
file_path = 'pure_prices.csv'
data = pd.read_csv(file_path)


# Предположим, что столбец с ценами называется 'price'
prices = data['Price']


# Вычисление средней цены
average_price = round(prices.mean(), 2)
print(f"Средняя цена: {average_price} руб.")


# Построение гистограммы
plt.hist(prices, bins=10, edgecolor='black')


plt.axvline(average_price, color='red', linestyle='dashed', linewidth=1)


# Добавление заголовка и меток осей
plt.title('Гистограмма цен')
plt.xlabel('Цена')
plt.ylabel('Частота')


# Показать гистограмму
plt.show()
