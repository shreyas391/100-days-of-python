#Day-4.3 Treasure map Exersice
row1 = ["1", "2", "3"]
row2 = ["2", "2", "3"]
row3 = ["3", "2", "3"]
map = [row1, row2, row3]
position = input("Where do you want to put the treasure map: ")
horizontal = int(position[0])
vertical = int(position[1])
a = map[vertical - 1]
b = a[horizontal - 1] = "X"
print(f"The 'X' is in {horizontal} column, {vertical} row.\n")
print(f"{row1}\n{row2}\n{row3}")
