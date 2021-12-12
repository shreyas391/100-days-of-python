#Day-7 Hangman Game Final Project
import random
import hangman_asci_art
import words
print(hangman_asci_art.logo)

some_words = words.word_list
word = random.choice(some_words)
blankes = []
for i in range(1, len(word) + 1):
  blankes.append("_")

lives = 7
while lives != 0 and "_" in blankes:
  user_guess = input("Guess any letter: ")
  for x in range(0, len(word)):  
      letter = word[x]
      if user_guess == letter:
        blankes[x] = letter
  print(blankes)
  if lives != 0:
    if user_guess not in word:
        lives -= 1
        print(f"You have {lives} lives left.")
        print(hangman_asci_art.stages[lives])
print(word)
