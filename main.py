print('Hi,PyCharm')
x = 43
y = 32
print(x*y)
print("End line")
def print_hi(name):

     print(f'Hi, {name}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import os
import time

directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
              f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')