a = int(input("Enter The Number"))
b = int(input("Enter The Number"))
c = int(input("Enter The Number"))

if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

print(f"Largest Number Is {largest}")