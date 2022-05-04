from tokenize import Number


n=int(input("what is Number"))
list=[]
for y in range(n):
    list.append(y)
print(list)
for num in range(n):
    a=list[num]
    r=(a*a)
    print(f"{r}\n")
