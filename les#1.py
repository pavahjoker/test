# https://www.youtube.com/watch?v=wDmPgXhlDIg&t=1301s

# Присваиваем значения переменным
name = 'Alise'  # Строковая переменная
age = 30        # Целочисленная переменная

# Выводим значения переменных, разделяя их символом ';'
print(name, age, sep=';')  # Вывод: Alise;30

# Присваиваем новые значения переменным
name1, age1 = 'Valentin', 31  # Множественное присваивание
print(name1, age1, sep='=')   # Вывод: Valentin=31

# Присваиваем переменной other_name значение переменной name
other_name = name  # Переменная other_name теперь содержит 'Alise'

# Выводим значения переменных, разделяя их символом '-'
print(other_name, age1, sep=' - ')  # Вывод: Alise-31

# Обмен значениями между переменными x и y
x = 3
y = 4
x, y = y, x  # Одновременное присваивание: x становится 4, y становится 3

# Выводим значения переменных x и y
print(x, y)  # Вывод: 4 3

# Присваиваем строковое значение переменной variable
variable = '123'

# Выводим тип переменной variable
print(type(variable))  # Вывод: <class 'str'> (показывает, что переменная variable имеет тип 'str')


# Создаем переменные x и y со значениями 5.5 и 10.2
x, y = 5.5, 10.2
# Суммируем значения переменных x и y в переменную summary
summary = x + y
# Выводим значение переменной summary
print(summary)

# Возведение в степень
x, y = 10, 5
z = x * y
print(z ** 2)

# Целочисленное деление
# Нужно 9 / 4 = 2 * 4 + 1
x, y = 9, 4
z = x // y
print(z)

# Остаток от деления
c = x % y
print(c)

# Числа с плавающей точкой можно сложить и тд. с другими числами
# Резульататом сложения будет число с плавающей точкой
my_int = 10
my_float = 5.5
print(my_int + my_float)
print(my_int * my_float)


# Переменная типа инт может хранить значение с 1000 нулями, 
# лишь бы хватило оперативной памяти
big_num = 10 ** 1000
print(big_num)



# чтоб получить переменную типа float из переменной типа int
# то нам нужно использовать функцию float() и передать ей переменную типа int
my_int = 10
my_float = float(my_int)
print(my_float)

# Чтоб получить переменную типа int из переменной типа float
# то нам нужно использовать функцию int() и передать ей переменную типа float
my_float = 10.5
my_int = int(my_float)
print(my_int)

# round() - округляет число до ближайшего целого
my_float = 10.6
my_int = round(my_float)
print(my_int)




# ** App #1 **
flat_number = int(input('Enter flat number: '))
entrance_number = ((flat_number-1) // 20 + 1)
flor_number = ((flat_number-1) % 20 // 4 + 1)
print( "Подьезд: " + str(entrance_number))
print( "Этаж: " + str(flor_number))