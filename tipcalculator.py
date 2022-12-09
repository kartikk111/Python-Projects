# Tip Calculator

total_bill = float(input("What was your total bill? \t "))

tip_percentage = 0.01 * int(input("What percentage tip would you like to give? 10, 12, or 15?\t"))

split = int(input("How many people to split the bill? \t"))

bill_with_tax = total_bill + (total_bill * tip_percentage)

amount = float(round((bill_with_tax / split), 2))

print(f"Each person should pay {amount}")