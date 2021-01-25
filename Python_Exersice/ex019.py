'''
    Make a program that randomizes one of
    four students to clear the blackboard
'''
from random import choice

name0 = str(input("Enter the student's name: ")).title()
name1 = str(input("Enter the student's name: ")).title()
name2 = str(input("Enter the student's name: ")).title()
name3 = str(input("Enter the student's name: ")).title()

list = [name0, name1, name2, name3]

print(f"This is the one whom will help the teacher out {choice(list)}")
