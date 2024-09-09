# https://www.youtube.com/watch?v=wDmPgXhlDIg&t=1368s
# lesson 7
# Индексы и слайсы

# ** App Lesson#1 **
flat_number = 25 # int(input('Enter flat number: '))
entrance_number = ((flat_number) // 20)
flor_number = ((flat_number) % 20 // 4)
print( "Подьезд: " + str(entrance_number))
print( "Этаж: " + str(flor_number))

fruits = ['apple', 'banana', 'cherry', 'fig', 'grape']
print(fruits[0])  # Outputs: 'apple'
print(fruits[1])  # Outputs: 'banana'
print(fruits[2])  # Outputs: 'cherry'
print(fruits[3])  # Outputs: 'fig'
print(fruits[4])  # Outputs: 'grape'
print(fruits[-4])  # Outputs: 'apple'

fruits[0] = 'pineapple'
print(fruits)  # Outputs: ['pineapple', 'banana', 'cherry', 'fig', 'grape'] 

fruits[0], fruits[4] = fruits[4], fruits[0]
print(fruits)  # Outputs: ['fig', 'banana', 'cherry', 'pineapple', 'grape']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:5])  # Outputs: [1, 2, 3, 4]
new_numbers = numbers[0:5]
new_numbers2 = numbers[:len(numbers)]
print(new_numbers)  # Outputs: [1, 2, 3, 4]
print(new_numbers2)  # Outputs: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[::-1])

print('\n')


# Три варианта как развернуть список:

# 1 
print(numbers[::-1])

# 2
numbers.reverse()
print(numbers)

nums2 = reversed(numbers)
print(nums2)
print(type(nums2))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums = list(reversed(numbers))
print(nums)