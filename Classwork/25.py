num = int(input("What Is The Number"))

def factorialNumber(num):
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        return factorial


def sumNumber(num):
    total = 0
    while (num > 0):
        rem = num % 10
        total = total + rem
        num = num // 10

    return total


if sumNumber(num) < factorialNumber(num):
    totalRev = 0

    while (num > 0):
        rem = num % 10
        totalRev = totalRev * 10 + rem
        num = num // 10

    print(f"{totalRev} Is Reverse")

def calculation(x,y):
    add=x+y
    subt=x-y
    return(add,subt)

print("enter the values:")
a=float(input())
b=float(input())
z1,z2 = calculation(a,b)

print("the sum:",z1)
print("the subtraction:",z2)
