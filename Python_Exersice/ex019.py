'''
    Make a program that randomizes one of
    .four students to clear the blackboard
'''
from random import choice

name = ["Gabriel", "Buh", "Jukes", "Jovi"]

print(f"This is the one whom will help the teacher out {choice(name)}")