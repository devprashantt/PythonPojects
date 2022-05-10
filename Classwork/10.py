number = int(input("What is the number\n"))

if number % 3 == 0 and number % 7 == 0:
    print("Hey")
elif number % 5 == 0 and number % 9 == 0:
    print("Hello")
else:
    print("Error")
