first = int(input('Введите число: '))
second = int(input('Введите чмсло: '))
third = int(input('Введите число: '))
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
