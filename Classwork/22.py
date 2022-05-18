# using function and for loop

def perfectFunction(n):
    n = int(input("Enter any number: "))
    sum1 = 0
    for i in range(1, n):
        if (n % i == 0):
            sum1 = sum1 + i

    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")

# using while loop

number = int(input("Please Enter any Number :- "))
i = 1
Sum = 0
while (i < number):
    if (number % i == 0):
        Sum = Sum + i
    i = i + 1

if (Sum == number):
    print("It is a Perfect Number")
else:
    print("It is not a Perfect Number")