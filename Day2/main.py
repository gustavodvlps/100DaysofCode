print("Welcome to the Tip Calculator")

#input variables
bill = float(input("What was the total bill? $ "))
people = int(input("How many people to split the bill? "))
percent = int(input("what percentage tip would you like to give? 10, 12, or 15? "))

#tip calculation
payforeach = ((bill * percent)/100 + bill)/people

#resut rounded out to two decimals
print("Each person should pay " + str(round(payforeach, 2)))