'''
    Make a program that calculates sine, cosine and tangent
'''
from math import sin, cos, tan, radians

angle = radians(float(input("Enter an angle: ")))

print(f"This is the result; Sine: {sin(angle):.2f}")
print(f"Cosine: {cos(angle):.2f}") 
print(f"and Tangent: {tan(angle):.2f}")
