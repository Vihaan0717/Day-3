name = input("Enter your name: " )
print("hello " + name)

price = 10
price = 20 # <--python always compile line by line so its last value should be 20 for price -->
print(price)

age = 20 # <--integer-->
is_new = True # <--boolean-->

name = input("What is your name? ")
print("so its you " + name + " right?")

name = input("What is your name? ")
color = input("what is your favorite color? ")
print(name + " likes " + color)

name = input("what is your age? ")
color = input("what is your favorite color? ")
print(name + " is " + color)

birth_year = input("birth year: ")
age = 2026 - int(birth_year)
print(age)

# <--type conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2026 - int(birth_year)
print(type(age))
print(age)

name = input("name =")
print("hello " + name)
