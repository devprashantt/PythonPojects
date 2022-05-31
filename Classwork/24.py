def firstLastSum(number):
    res = number % 10

    # Now, continue a loop until
    # the number becomes less than 9.
    while number > 9:
        number = number // 10

    res += number

    print('Addition of first and last digit of number is', res)


number = int(input("What Is The Number"))
firstLastSum(number)