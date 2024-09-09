# https://www.youtube.com/watch?v=wDmPgXhlDIg&t=1368s
# Lesson 5
# форматирование cтрок

name = 'Alice'
age = 25
print(f"My name is {name} and I'm {age} years old.")


x = 10
y = 5

print(f"{x + y} != {x * y}")
print(f"{x} + {y} = {x + y}")

# Задача

my_string = '25' # input("Enter a string: ")

if my_string.isdigit():
    my_integer = int(my_string)
    print(my_integer)
else:
    print(f" {my_string} is not a number")


# В Python существуют два основных способа форматирования строк: 
# через метод .format() и оператор %. 
# Вот объяснение и примеры для каждого из них.

# 1. Метод .format()
# Метод .format() — более современный и гибкий способ вставки значений в строку.


name = 'Вася'
name2 = 'Хуй'
print('строка с {}, ну и строка с {}'.format(name, name2))

name = "Alex"
age = "30"
text = "My name is {} and I am {} years old.".format(name, age)
print(text)

# Аргументы по порядку:
text = "My name is {} and I am {}.".format("Alex", 30)
print(text)

# Именованные аргументы:
text = "My name is {name} and I am {age}.".format(name="Alex", age=30)
print(text)

# Индексация позиций:
text = "My name is {0} and I am {1}. {0} is learning Python.".format("Alex", 30)
print(text)


# 2. Оператор %
# Этот способ форматирования строк пришел из языка C и является старым методом, который всё ещё используется.

# Форматы для %:
# %s — для строк.
# %d — для целых чисел.
# %f — для чисел с плавающей точкой.

# My example:
name = 'Antua'
name2 = 'Alex'
age = 25
string = 'строка с %s и тут вдруг еще один %s ну и хуев им пачку - %d' % (name, name2, age)
print(string)


# GPT Пример:
name = "Alex"
age = 30
text = "My name is %s and I am %d years old." % (name, age)
print(text)

# Общая форма спецификатора для числа с плавающей точкой:
# %.nf — где n — это количество знаков после запятой.
# Пример с плавающей точкой:
pi = 3.14159
text = "The value of pi is approximately %.12f." % pi
print(text)


# Сравнение:
# Метод .format() более гибок и может принимать как позиционные, так и именованные аргументы.
# Оператор % проще и удобен для простых случаев, но не столь универсален и расширяем, как .format().

# Рекомендация:
# Для современных проектов лучше использовать метод .format() 
# или новый способ форматирования через f-строки (Python 3.6+), 
# например:
name = "Alex"
age = 30
text = f"My name is {name} and I am {age} years old."
print(text)