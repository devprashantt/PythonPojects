
n=int(input("Enter number: "))

temp=n
rev=0

while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10

if(temp==rev):
    total = 0
    while (temp != 0):
        rem = temp % 10
        total = (total + rem)
        temp = temp // 10
    print(f"{total} Is Total Sum")
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")