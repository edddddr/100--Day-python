
student_height = input("A list student height : ").split()


for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])


count = 0
sum= 0
for n in student_height:
  sum +=n 
  count +=1

avg = sum / count
print(f"Average legnth is: {round(avg, 2)}") 


