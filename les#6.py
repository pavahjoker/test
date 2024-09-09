# https://www.youtube.com/watch?v=wDmPgXhlDIg&t=1368s
# Lesson 6
# list

fruits = ['apple', 'banana', 'cherry']
print(fruits)  # Outputs: ['apple', 'banana', 'cherry']

print(len(fruits))  # Outputs: 3

my_list = list()
print(my_list)  # Outputs: []

# dont work with this
my_list = [1, "apple", True, 1.5, [1, 2, 3]]
print(my_list)  # Outputs: [1, 'apple', True, 1.5, [1, 2, 3]]

# == 
my_list1 = [1, 2, 3]
my_list2 = [1, 3, 2]
my_list3 = [1, 2, 3]
print(my_list1 == my_list2)  # Outputs: False
print(my_list1 == my_list3)  # Outputs: True

print(bool([]))  # Outputs: False
print(bool([0]))  # Outputs: True

print('banana' in fruits)  # Outputs: True
print('watermelon' in fruits)  # Outputs: False


element1 = 'apple'
element2 = 'banana'
element3 = 'cherry'
my_list = [element1, element2, element3]
print(my_list)  # Outputs: ['apple', 'banana', 'cherry']

word = 'hello pidor'
my_list = list(word)
print(my_list)  # Outputs: ['h', 'e', 'l', 'l', 'o']

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list3 = my_list1 + my_list2
print(my_list3)  # Outputs: [1, 2, 3, 4, 5, 6]

fruits = ['apple', 'banana', 'cherry']
fruits2 = 'watermelon' + ' and zalupa kentavra'
fruits.append(fruits2)
print(fruits)  # Outputs: ['apple', 'banana', 'cherry', 'watermelon and zalupa kentavra']

fruit = fruits.pop()
print(fruit)  # Outputs: 'watermelon and zalupa kentabra'
print(fruits)  # Outputs: ['apple', 'banana', 'cherry']

fruits1 = ['apple', 'banana', 'cherry']
fruits2 = ['fig', 'grape']
fruits1.extend(fruits2)
print(fruits1)  # Outputs: ['apple', 'banana', 'cherry', 'fig', 'grape']

fruits1.reverse()
print(fruits1)  # Outputs: ['grape', 'fig', 'cherry', 'banana', 'apple']

my_list = [5, 4, 8, 10, 1, 2, 14, 4]
my_list.sort()
print(my_list)  # Outputs: [1, 2, 4, 4, 5, 8, 10, 14]
my_list.sort(reverse=True)
print(my_list)  # Outputs: [14, 10, 8, 5, 4, 4, 2, 1]

my_string = 'My name is Elton John'
my_list = my_string.split(" ")
print(my_list)  # Outputs: ['My', 'name', 'is', 'Elton', 'John']


joined_string = ' '.join(my_list)
print(joined_string)  # Outputs: My name is Elton John
my_list = [2, 5, 0, 7, 3, 9, 46]
print(max(my_list))  # Outputs: 46
print(min(my_list))  # Outputs: 0