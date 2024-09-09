# https://www.youtube.com/watch?v=wDmPgXhlDIg&t=1368s
# Lesson 4
# (str) - Строковый тип данных
# Определите строку с помощью одинарных кавычек
my_str = 'Hello, World!'
print(my_str)

# Определите строку с помощью двойных кавычек
my_str = "Hello, World!"
print(my_str)


# Определите строку с помощью тройных кавычек (многострочная строка)
my_str = '''Hello, World!'''
print(my_str)


# Объедините две строки для формирования полного имени
first_name = 'Alice'
last_name = 'Smith'
full_name = first_name + ' ' + last_name
print(full_name)


# Получите длину строки (количество символов)
length = len(full_name)
print(length)


# Преобразуйте целое число в строку
my_integer = '10' # целое число в виде строки
my_string = str(my_integer)
print(type(my_string)) # тип - строка
print(int(my_integer)) # преобразование строки в целое число
my_int = int(my_integer)
print(type(my_int)) # тип - целое число


# Ввод строки с клавиатуры (закомментировано)
# my_string = input('Enter a number: ')
# print(type(my_string)) # тип - строка


# Вычислите большое целое число и получите количество его цифр
big_int = 2 ** 5000
print(len(str(big_int))) # количество цифр в big_int


# Проверьте, содержится ли подстрока в строке
my_string = "Hello world"
print("hello" in my_string) # True, если подстрока найдена


# Проверьте, содержится ли подстрока в строке
my_string = "Hello world"
print("hello" not in my_string) # False, если подстрока не найдена


my_string = "    Hello, World!                 "
print(my_string.upper()) # верхние буквы
print(my_string.lower()) # нижние буквы
print(my_string.strip()) # удаляет пробелы в начале и конце строки
print(my_string.lstrip()) # удаляет пробелы в начале строки
print(my_string.rstrip()) # удаляет пробелы в конце строки
print(my_string.replace("Hello", "Bye")) # заменяет подстроку в строке
print(my_string.split(",")) # разбивает строку на подстроки по запятой
print(my_string.find("Hello")) # ищет подстроку в строке и возвращает её позицию
print(my_string.count("rl")) # подсчитывает количество вхождений подстроки в строку
print(my_string.isalpha()) # проверяет, является ли строка буквами
print(my_string.isdigit()) # проверяет, является ли строка цифр


integer = input("Enter a number: ")
if integer.isdigit():
    integer = int(integer)

print(type(integer))

