n = int(input("Upto Which You Want To Add\n"))

fact = 1
sumOfSeries = 0

for i in range(n+1):
    for j in range(1,i+1):
        fact = fact * j
    print(fact)
    sumOfSeries = sumOfSeries + fact

print(sumOfSeries)
