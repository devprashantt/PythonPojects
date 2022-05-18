n1 = int(input("What Is The 1st Number\n"))
n2 = int(input("What Is The 2nd Number\n"))

for i in range(n1,n2+1):
    if(i>1):
        for j in range(2,i):
            if i%j == 0:
                print(f"{i} Is Not A Prime Number")
                break
            else:
                print(f"{i} Is a Prime Number")

# Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for z in range(2, num):
           if (num % z) == 0:
               break
       else:
           print(num)