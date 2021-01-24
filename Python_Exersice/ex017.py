'''
    Make a program that calculates Hypotenouse
'''

from math import pow,sqrt

x = float(input("Enter a number: "))
y = float(input("Enter another one: "))

h = sqrt(pow(x,2) + (pow(y,2)))

print(f"This is the result {h:.2}")
