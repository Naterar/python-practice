print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_decimal = tip / 100
total_with_tip = bill * (1 + tip_as_decimal)
bill_split = total_with_tip / people
print(f"Each person should pay ${round(bill_split, 2)}")
