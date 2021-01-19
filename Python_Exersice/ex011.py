'''
    Make a program that reads a wall's width and height 
    and calculate its area and how much ink will be necessary to paint it.
'''

wallw = float(input("What is the width of your wall? "))
wallh = float(input("What is the height of your wall? "))
    
print(f"The area of your wall is {wallw*wallh}m2 and it will be necessary {(wallw*wallh)/2} Lt of ink.")