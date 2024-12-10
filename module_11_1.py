import pandas as pd

data = pd.read_csv("data.csv")
mean_value = data['column_name'].mean()
print(f"Среднее значение в столбце 'column_name':{mean_value}")
print(data.describe())

filtered_data = data[data['column_name'] > mean_value]
print(filtered_data)

import numpy as np

array = np.array([1,2,3,4,5])
sum_array = np.sum(array)
mean_array = np.mean(array)
squared_array = np.square(array)

print(f"Сумма масива:{summ_array}")
print(f"Среднее значение массива: {mean_array}")
print(f"Квадраты элементов массива: {squard_array}")

import matplotlib.pyplot as plt

x = np.array(range(1,6))
y = np.array([1,4,9,16,25])

plt.plot(x, y, marker='0')
plt.title("Пример линейного графика")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()

plt.savefig("plot.png")
plt.show()