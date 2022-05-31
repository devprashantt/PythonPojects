number = int(input("What Is The Number \n"))

totalSum = 0

while number != 0:
    rem = number % 10
    totalSum = totalSum + rem
    number = number//10

factorial = 1

for i in range(1, totalSum + 1):
    factorial = factorial * i

print(f"Sum Is {totalSum}\nFactorial Is {factorial}")