students_height=input("what is your height-").split()
for n in range(0,len(students_height)):
    students_height[n]=int(students_height[n])
print(students_height)

total_height=0
for height in students_height:
    total_height+=height
print(total_height)

students_number=0
for count in students_height:
    students_number+=1
print(students_number)

average_height=total_height/students_number
print(average_height)

# answer

# [140, 150, 160]
# 450
# 3
# 150.0