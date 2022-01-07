# Learn Python Coding in 2021
#############################

#Working with (master)
	#cd /c/pythonstuff

#Saving changes on GitHub
	#git add .
	#git commit -am "Text"
	#git push

# Clear the terminal screen
import os
os.system('clear')

# String
first_name = "John"

# Number
age = 41

# List
# Computer always starts with 0
#			0	   1	  2	     3
names = ["John", "Bob", "Mary", 41]

print(names)
print(names[0])

# Tuples = list, that you can´t change (add, delete, ...)
names = ("John", "Bob", "Mary")

print(names)
print(names[0])

# Dictionaries
fav_pizza = {
	"John": "Pepperoni",
	"Bob": "Mushroom",
	"Mary": "Cheese"
	}

print(fav_pizza["Mary"])

#Boolean
name = True

print(name)

#Strings
greetings_1 = 'My Boss Yelled "GET BACK TO WORK!"'
greetings_2 = "My Boss Yelled 'GET BACK TO WORK!'"
greetings_3 = "My Boss Yelled \"GET BACK TO WORK!\""	#Backslash = alt+92
greetings_4 = "My Boss Yelled \n\"GET BACK TO WORK!\""	# n make GET BACK TO WORK! on another line

print(greetings_1)
print(greetings_2)
print(greetings_3)
print(greetings_4)

name = "John"
greet = "Hello, my name is " + name 	# Has to be string + string, not string + number

print(greet)

greet = "Hello, my name is John Elder"

print(greet.upper())
print(greet.lower())

greet = "hello, my name is John Elder"

print(greet.capitalize())	# all letters uppercase
print(greet.title())		# all first letters uppercase
print(greet.swapcase())		# big are small and small are big
print(len(greet))			# lenght of string
print(greet[13])			# 13th character in string
print(greet[18:22])			# 18th to 22nd character
print(greet.split(" "))		# make list of items from string
print(greet.split(" ")[5])	# print just 5th item in string
print(greet.split(" ")[4:6])	# just John and Elder in list

#Numbers
	# 10 = integer
	# 10.25 = float

num = 10

print(num)
print(float(num))	#integer -> float

num = 10.25

print(int(num))		#float -> integer
print(7+2)
print(2*2)
print(5/2)
print(2**9)		#2 to the power of 9th (dvě na druhou)
print(10%3)		#remainder after 10 divided by 3 (zbytek)

num_1 = 5
num_2 = 2

print(num_1 * num_2)

num = "5"

print(num * 3)			# 555
print((int(num)) * 3)	# string -> integer

#Lists

names = ["John", "Bob", "Tina"]
names[0] = "Henis"					# replaces John by Henis on 0 position
names.append("DJ")					# add DJ to list
names.append(69)

print(names)
print(names[0])
print(names[3])
print(names[4] * 5)
print(names * 2)

nums = [1, 2, 3, 4, 5]
other_name = "Hergot"
names = ["Okamura", other_name, nums]

print(names)
print(names[2])
print(names[2][2])		# 3rd item in 3rd item in list
print(names[2][2] + 9)
print(len(names))
print(names[len(names) - 1])

#Tuples

names = ("John", "Bob", "Tina")

print(names)
print(names[0])

tuple1 = ("John", "Bob", "Tina")
tuple2 = ("Mery",)
tuple3 = tuple1 + tuple2			# This way can be tuple changed
tuple4 = tuple1[0:2]

print(tuple1)
print(tuple3)
print(tuple1[0:2])
print(tuple4)