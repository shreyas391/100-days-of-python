#Day-3 Treasure Hunting Game Final Project
print("Welcoming you heartly to the Treasure Hunting Game!\n")
road = input("There are two roads in front of you which you would like to choose 'left' or 'right'? ")
if road == "left" or road == "L":
  sea = input("You are now reached to the sea Type 'swim' to swim across the sea or Type 'wait' to wait for the boat? ")
  if sea == "wait":
    doors = input("You arrive to the island unharmed. there is three doors in front of you which you would like to open 'red', 'yellow' either 'blue'? ")
    if doors == "yellow":
      print("Wow! you found the treasure good work.")
    elif doors == "blue":
      print("Ohhh no! there are very cruel animals in here you are dead\nGame over!")
    elif doors == "red":
      print("Ohhh no! the room is full of fire. you are burned\nGame over!")
    else:
      print("Hmmm i think you typed something wrong please check your answer again.")
  elif sea == "swim":
    print("Ohhh no! there is a shark in this way. You are dead\nGame over!")
  else:
    print("Hmmm i think you typed something wrong please check your answer again.")
elif road == "right" or road == "R":
  print("Ohhhh no! there is an lion in this way. You are dead\nGame over!")
else:
  print("Hmmm i think you typed something wrong please check your answer again.")
