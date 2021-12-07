#Day-3.4 Pizza Order Exersice
print("Welcome to the Python Pizza Deliveries!")
size = input("What size Pizza do you want? S, M, or L: ")
pepperoni = input("Do you to add pepperoni? Y or N: ")
extra_cheese = input("Do you want us to add extra cheese? Y or n: ")
bill = 0

if size == "S":
  bill = 15
  if pepperoni == "Y":
    bill += 2
elif size == "M":
  bill = 20
  if pepperoni == "Y":
    bill += 3
elif size == "L":
  bill = 25
  if pepperoni == "Y":
    bill += 3
if extra_cheese == "Y":
  bill += 1

print(f"Your total bill was: ${bill}")
