# First Python Program

import datetime
print('Please enter your Name: ')
name = input()

print('What is your age: ')
age = input()

print('User Details ...')
print('Name: ', name)
print('Name Length: ', len(name))
print('Age: ', age)


# Literal String Interpolation or more commonly as F-strings
print('*'*10, 'F Strings', '*'*10)

print(f"Hello, My name is {name} and I'm {age} years old.")
print(f"{datetime.datetime.today():%B %d, %Y}")

# Formatting is now handled by calling .format() on a string object.
print('*'*10, 'String.format()', '*'*10)\

greeting = "Hello, My name is {} and I'm {} years old."
print(greeting.format(name, age))

greeting = "Hello, My name is {} and I'm {} years old. Today is {}."
print(greeting.format(name, age, "Monday"))
