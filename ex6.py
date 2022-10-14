# Strings and Text

# Creating a variable and assigning it a numerical value
types_of_people = 10

# Creating a variable and assigning it an f-string which includes a variable
x = f"There are {types_of_people} types of people."

# Assign two strings to two variables
binary = "binary"
do_not = "don't"
# Create a variable and assign an f-string which includes a variable in it
y = f"Those who know {binary} and those who {do_not}."

# Display values of the variables
print(x)
print(y)

# Display an f-string with a variable
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Assign values to variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Display a string using .format() syntax
print(joke_evaluation.format(hilarious))

# Assign values to variables
w = "This is the left side of..."
e = "a string with a right side."

# Display the concatenation of variables 
print(w + e)
