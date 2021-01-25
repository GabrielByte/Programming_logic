'''
    Make a program that the order of a seminary
'''
from random import shuffle

name0 = str(input("Enter the student's name: "))
name1 = str(input("Enter the student's name: "))
name2 = str(input("Enter the student's name: "))
name3 = str(input("Enter the student's name: "))

list = [name0, name1, name2, name3]
shuffle(list)

print(f"This will be the order {list}")