print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

z=name1+name2

y=z.lower()

c=y.count("t")
d=y.count("r")
e=y.count("u")
f=y.count("e")

true=c+d+e+f

g=y.count("l")
h=y.count("o")
i=y.count("v")
j=y.count("e")

love=g+h+i+j

love_score=int(str(true)+str(love))


if love_score<10 or love_score>90:
    print(f"your love score is {love_score} go and do party")
elif love_score>=40 and love_score<=50:
    print(f"your score is {love_score} u are alright")
else:
    print(f"your score is {love_score}")


# answer
# Welcome to the Love Calculator!
# What is your name? 
# PRASHANTKUMARSINGH
# What is their name? 
# SEETASINGH
# your score is 72