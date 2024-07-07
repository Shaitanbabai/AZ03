import matplotlib.pyplot as plt
import numpy as np

x = [2, 4, 6, 8, 10, 12]
y = [3, 9, 12, 15, 18, 21]

plt.plot(x, y)

plt.title("Linear graph")
plt.xlabel("Axe X")
plt.ylabel("Axe y")

plt.show()

data = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 4, 5, 8, 8, 8]

plt.hist(data, 4)  # bins - количество интервалов

plt.title("Linear graph")
plt.xlabel("Axe X")
plt.ylabel("Axe y")

plt.show()

# a = np.linspace(0, 12, 10)
# print(a)

# x = np.linspace(-10, 10, 100)
# y = x**2
# plt.plot(x, y)
# plt.title("Graph y=x**2")
# plt.xlabel("Axe X")
# plt.ylabel("Axe y")
# plt.grid(True)
# plt.show()

