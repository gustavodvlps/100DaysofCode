print("Welcome to the Tip Calculator")

#input variables
bill = float(input("What was the total bill? $ "))
people = int(input("How many people to split the bill? "))
percent = int(input("what percentage tip would you like to give? 10, 12, or 15? "))

#tip calculation using round function to two decimals
payforeach = ((bill * percent)/100 + bill)/people
finalamount = round(payforeach, 2)

print(f"Each person should pay {finalamount}")