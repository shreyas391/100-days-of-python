#Day-5.1 Average Height Exersice
lenght = 0
student_height = input("Type all students heights: ").split()
for n in range(0, len(student_height)):
  student_height[n] = int(student_height[n])
  lenght += 1

total_height = 0
for height in student_height:
  total_height += height

average_height = round(total_height / lenght)
print(average_height)
