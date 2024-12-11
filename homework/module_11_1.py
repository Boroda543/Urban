import requests

response = requests.get('https://api.github.com')
data = response.json()
print(data)

import  pandas as pd

data = pd.read_csv(r'D:\проэкт урбан\pythonProject2\data.csv')
print(data.head())

mean_value = data['name']
print(mean_value)

import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,5,7,11]
plt.plot(x, y, marker='1')
plt.title('Пример графика')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()