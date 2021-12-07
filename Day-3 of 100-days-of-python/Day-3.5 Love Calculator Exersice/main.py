#Day-3.5 Love Calculator Exersice
print("Welcome to Python Love Calculator!")
name1 = input("Enter your name please: ").lower()
name2 = input("Enter their name please: ").lower()
combained = name1 + name2

t = combained.count("t")
r = combained.count("r")
u = combained.count("u")
e = combained.count("e")
true = t + r + u + e

l = combained.count("l")
o = combained.count("o")
v = combained.count("v")
e = combained.count("e")
love = l + o + v + e

love_score = str(true) + str(love)
result = int(love_score)
if result >= 80:
  print(f"Your love score is: {result}%, you go together like coke and mentos.")
elif result >= 50:
  print(f"Your love score is: {result}%, you are alright together.")
else:
  print(f"Your love score is: {result}%")
