#Day-8.2 Prime Number Checker
n = int(input("Check this number: "))

def prime_checker(number):
  is_prime = True
  for i in range(2, number - 1):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("it's not a prime number")
prime_checker(number = n)
