#Day-5 Pypassword Generator Exersice Final project
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "/", "?", "|"]
print("Welcome to the Pypassword Generator!")
in_letters = int(input("How many letters would you like in your password? "))
in_numbers = int(input("How many numbers would you like in your password? "))
in_symbols = int(input("How many symbols would you like in your password? "))

total = [letters, numbers, symbols]
password = []
for char in range(0, in_letters):
  password += random.choice(letters)

for num in range(0, in_numbers):
  password += random.choice(numbers)

for sym in range(0, in_symbols):
  password += random.choice(symbols)

final = ""
random.shuffle(password)
for s in password:
  final += s
print(final)
