my_dict = {'Denis': 1985, 'Kolia': 2003, 'Oleg': 1960}
my_dict['Olesia'] = 2010
my_dict['Pavel'] = 1986
my_dict['Roman'] = 2007
del my_dict['Denis']
print(my_dict)
print(my_dict['Oleg'])
print(my_dict['Olesia'])
my_set = {1, 2, 1, 2, 'korova', True, 'korova'}
print(my_set)
print(my_set.add(5))
print(my_set.add(7))
print(my_set.discard(1))
print(my_set)
