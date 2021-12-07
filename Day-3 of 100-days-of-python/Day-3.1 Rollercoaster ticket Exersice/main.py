#Day-3.1 Rollercoaster ticket Excersice
print("Welcome to our collercoaster ride!")
height = int(input("What is your height tell us in cm: "))
bill = 0
if height >= 120:
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
  elif age <= 18:
    bill = 7
  elif age >= 45 and age <= 55:
    bill = 0
  else:
    bill = 12
  photos = input("Do you want a photo taken type 'Y' or 'N': ")
  if photos == "Y":
    total_bill = bill + 3
    print(f"Your total bill was: ${total_bill}")
  else:
    print(f"Your total bill was: {bill}")
else:
  print("Sorry, you have to grow taller if you want to ride in rollercoaster")
