''' 
    Make a program that reads something 
    and shows your datatype and every possible informations.
'''

x = input("Type something here: ")

print(f"The datatype of is... {type(x)}")
print(f"Is {x} an character? {x.isalpha()}")
print(f"Is it alphanumeric? {x.isalnum()}")
print(f"Is it a number? {x.isnumeric()}")
print(f"Is it upper case? {x.isupper()}")
print(f"Is it lower case? {x.islower()}")
print(f"Does it have space? {x.isspace()}")
