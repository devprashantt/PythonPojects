students_height=input("what is your height-").split()
for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])
print(students_height)
height=0
for number in students_height:
    if number>height:
        height=number
print(height)