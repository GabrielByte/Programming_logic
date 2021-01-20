'''
    Make a program that gets the car's mileage and
    how many days is was used. 
    And the program has to show how much it will cost,
    considering the cost is R$60.00 bucks per day and R$00.15 per mile drove. 
'''

days = int(input("How many days did you drive? "))
km = float(input("How many mile did you drive? "))

print(f"You're gonna have to pay {(days * 60) + (km * 00.15)} bucks")