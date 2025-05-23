

student_height = input("A list student height : ").split()


for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

print(student_height)

highest_score = 0

for n in student_height:
   if heighest_score < n:
       heighest_score = n
   else:
       heighest_score

print(f"The higest score in the class is: {heighest_score}")
       

