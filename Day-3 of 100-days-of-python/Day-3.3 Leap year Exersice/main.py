#Day-3.3 Leap year Exersice
year = int(input("which year would you like to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"{year} is an leap year")
    else:
      print(f"{year} is not an leap year")
  else:
    print(f"{year} is an leap year")
else:
  print(f"{year} is not an leap year")
