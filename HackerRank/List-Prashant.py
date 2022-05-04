import random
x=int(input("number1\n"))
y=int(input("number2\n"))
z=int(input("number3\n"))
n=int(input("number4\n"))
output = [];
abc = [];
for X in range(x+1):
    for Y in range(y+1):
        for Z in range(z+1):
            if X+Y+Z != n:
                abc = [X,Y,Z];
                output.append(abc);
print(output);    
    