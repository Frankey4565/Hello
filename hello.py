# Clear the terminal screen
import os
os.system('clear')

# Sting
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