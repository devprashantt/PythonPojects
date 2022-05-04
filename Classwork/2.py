# average of number

# w = (input('What is your Name\n'))
# x = int(input('What is marks in the 1st Subject\n'))
# y = int(input('What is marks in the 2nd Subject\n'))
# z = int(input('What is marks in the 3rd Subject\n'))
# a = int(input('What is marks in the 4th Subject\n'))
# b = int(input('What is marks in the 5th Subject\n'))
# print(f"Average Is {(x + y + z + a + b) / 5} & name is {w}")

Total = 0
w = (input('What is your Name\n'))
for i in range(5):
    i = int(input(f"Enter {i + 1} Number\n"))
    Total = (Total + i) / 5
print(f"Sum is {Total} & Name is {w}")
