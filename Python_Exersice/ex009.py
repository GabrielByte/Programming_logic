'''
    Make a program that takes a number and shows its mutiplication table
'''

n1 = int(input("Enter a number: "))
n2 = 1

while n2 <= 10:
    n3 = n1 * n2
    print(f"{n1} x {n2} = {n3}")
    n2 += 1