'''
    Make a program that reads a product's price and shows a new price 
    5% OFF
'''

product = float(input("What is the price of that? "))

print(f"That cost {product} bucks but now is {product - (product * 5/100)} bucks")