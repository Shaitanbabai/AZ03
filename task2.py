import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100  # Количество образцов
data_x = np.random.rand(num_samples)
data_y = np.random.rand(num_samples)

# Печать примера массива случайных чисел
random_array = np.random.rand(5)  # Массив из 5 случайных чисел
print("Пример массива случайных чисел:", random_array)

# Создание диаграммы рассеяния
plt.scatter(data_x, data_y, alpha=0.5, edgecolor='w', s=50)
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('X значения')
plt.ylabel('Y значения')

# Отображение диаграммы рассеяния
plt.show()
