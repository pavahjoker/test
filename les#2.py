# https://www.youtube.com/watch?v=wDmPgXhlDIg&t=1368s
# Lesson 2
# Булевый тип данный (bool)

is_student = True
print(is_student)
is_graduated = False
print(is_graduated)

print('\n')

x = 10 
y = 10
print(x == y)
# результат выражения = True
not_equal = x != y # оператор "не равно" !=
print(not_equal)
# результат выражения = False

print('\n')

x = 10
y = 9
print(x > y)
# результат выражения = True
print(x < y)
# результат выражения = False
print(x >= y)
# результат выражения = True
print(x <= y)
# результат выражения = False

print('\n')

x = 10
y = 10
print(x >= y)
print(x <= y)

print('\n')

x = 1
 # Оператор "И" and
print(x < 5 and x > -2)

# Оператор not 
print(not x < 5 and x > -2)

print('\n')

# функция bool() преобразует значение в булевый тип
# 
print(bool(-1))
print(bool("Хелло мир"))
print(bool(0))