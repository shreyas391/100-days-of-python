#Day-8 caesar cipher Final Project
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

i = 0
while i == 0:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type shift number:\n"))

  def caesar(message, shift_num, direction):
    final_text = ""
    for x in range(0, len(message)):
      if message[x] in alphabets:
        index = alphabets.index(message[x])
        if direction == "encode":
          shifted = alphabets[index + shift_num]
        elif direction == "decode":
          shifted = alphabets[index - shift_num]
        final_text += shifted
      else:
        final_text += message[x]
    print(f"Your {direction}d text is: {final_text}")

  caesar(text, shift, direction)
  continues = input("If you want to encrypt or decrypt again please type 'no' or 'yes': ")
  if continues == 'no':
    i = 1
