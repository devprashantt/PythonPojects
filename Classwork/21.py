n1 = int(input("What Is The Number\n"))

totalRev = 0

while(n1>0):
    rem = n1 % 10
    totalRev = totalRev*10 + rem
    n1 = n1 // 10

print(f"{totalRev} Is Reverse")