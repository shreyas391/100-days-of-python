#Day-2 Final project Tip calculator
print("Welcome to tip calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15: "))
total_bill = (tip / 100 * bill) + bill
persons = int(input("How many persons to split the bill? "))
result = round(total_bill / persons, 2)
print(f"Each person should pay: {result}")
