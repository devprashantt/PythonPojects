print("welcome to roller coasyer coaster")
a=int(input("what is ur height-"))
bill=0
if a>120:
  print("u can ride")
  age=int(input("what is ur age-"))
  if age<12:
      bill=5
      print("please pay 5 dollor")
  elif age<=18:
      bill=7
      print("please pay 7 dollor")
  elif age>=45 and age<=60:
      print("free ride")
  else:
      bill=12
      print("please pay 12 dollor")
  photo=input("do u want photo taken? Y or N ")
  if photo=="Y":
    bill+=3
    print(f"your bill is {bill}")

else:
  print("u can not ride")


# welcome to roller coasyer coaster
# what is ur height-140
# u can ride
# what is ur age-18
# please pay 7 dollor
# do u want photo taken? Y or N Y
# your bill is 10

