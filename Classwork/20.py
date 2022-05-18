n1 = int(input("What Is The Number"))

total = 0

while(n1>0):
    rem = n1%10
    total = total + rem
    n1 = n1//10

print(f"{total} Is Total Sum")
