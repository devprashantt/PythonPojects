year = int(input("Which year do you want to check? "))
if year%100==0:
    if year%400==0:
        print("Leap year")
    else:
        print("Not a leap year")
elif year%4==0:
    print("Leap year")
else:
    print("Not leap year")


# answer

# Which year do you want to check? 1900
# Not a leap year

# Which year do you want to check? 2000
# Leap year




