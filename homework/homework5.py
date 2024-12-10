immutable_var= 1,'strig',6,5,True
print(immutable_var)
immutable_var[0]=100 # Нельзя изменить элемент кортежа потому что элементы кортежа не изменяемы
mutable_list=[7,'strig',True,7.8]
mutable_list[0]=1
print(mutable_list)