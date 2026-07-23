"""These are strings"""
first='john'
second='smith'
message = first +' [' +second+ '] is the coder'
print(message)
"""let's find the word in a string"""
course = 'python for beginners'
print('python' in course)
"""Lets find the length of the string"""
course = 'python for beginners'
print(len(course))
"""Lets find the index of a string"""
course = 'python for beginners'
print(course.find('p'))
"""Lets replace the string"""
course = 'python for beginners'
print(course.replace('beginners','absolute beginners'))
"""Lets now make it upper case"""
course = 'python for beginners'
print(course.upper())
"""Lets make it lower case"""
course ='python for beginners'
print(course.lower())

"""Lets make the operators"""
a=15
b=20
"""addition"""
print(a+b)
"""subtraction"""
print(a-b)
"""multi"""
print(a*b)
"""division"""
print(a/b)
"""Floor"""
print(a//b)
"""modules"""
print(a%b)
"""power"""
print(a**b)

"""Lets start from if statements"""
is_hot = True
is_cold = False

if is_hot:
    print("Its a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("Its a cold day")
    print("Wear warm clothes")
else:
    print("Its a lovely day")
    print("Enjoy your day")

"""23-07-26//Lets start with if/elif/else and length of string"""
name = "J"
if len(name) < 3:
    print('Name must be at least 3 characters')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('Name looks good!')