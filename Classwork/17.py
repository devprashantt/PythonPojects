import math

n = int(input("What Is The Number\n"))
total = 0

for i in range(1,n+1):
    exponent = pow(i,i)
    if i%2 == 0:
        total = total - exponent
    else:
        total = total + exponent

print(total)

squareRoot = math.sqrt(n)
print(squareRoot)