num1 = int(input("What is the number\n"))
num2 = int(input("What is the number\n"))
num3 = int(input("What is the number\n"))

min = 0
while num1 and num2 and num3:
    num1 = num1 - 1
    num2 = num2 - 1
    num3 = num3 - 1
    min = min + 1

print(min)

def minimum(x,y,z):
    min = 0
    while num1 and num2 and num3:
        num1 = num1 - 1
        num2 = num2 - 1
        num3 = num3 - 1
        min = min + 1

    return min

num1 = int(input("What is the number\n"))
num2 = int(input("What is the number\n"))
num3 = int(input("What is the number\n"))

print(f"(Minimum Number Is {minimum(num1,num2,num3)})")