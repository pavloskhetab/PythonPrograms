# More Variables and Printing
name = 'Zed A. Shaw'
age = 40 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# An inch is 2.54 cm and a kilo is 2.2046 lbs
height_inch_to_cm = round(height * 2.54)
weight_lbs_to_kilo = round(weight / 2.2046)

print(f"Let's talk about {name}.")
print(f"He's {height_inch_to_cm} cm tall.")
print(f"He's {weight_lbs_to_kilo} kilos heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
