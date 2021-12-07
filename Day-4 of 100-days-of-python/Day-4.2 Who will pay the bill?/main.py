#Day-4.2 Who will pay the bill?
import random
name = input("Enter all persons name: ")
split_name = name.split(", ")
random_int = random.randint(0, len(split_name))
person = split_name[random_int - 1] 
print(f"{person} has to pay the bill.")
