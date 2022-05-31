n1 = int(input("What Is The Number"))

total = 0

while(n1>0):
    rem = n1%10
    total = total + rem
    n1 = n1//10

print(f"{total} Is Total Sum")

num = int(input("Enter a number ( greater than 1)"))
f = 0
i = 2
while (i <= num / 2):
    if num % i == 0:
        f = 1
        break
    i = i + 1

if f == 0:
    print("The entered number is a PRIME number")
    count = 0
    while (num != 0):
        num //= 10
        count += 1
    print(f"Number Of Digits {count}")

else:
    print("The entered number is not a PRIME number")


