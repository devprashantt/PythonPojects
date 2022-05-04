print("welcome to treasure land")
print("your misssion is to calculate tresure land")
choise1=input('you\'re at the crossland ,where do u want to go? type "left" or "right".').lower()

if choise1=="left":
   choise2=input('''you've come to a lake . there is an island in the middle of the lake.type "wait" to wait for a boat. type "swim" to swim accross the river''').lower()
   if choise2=="wait":
      choise3=input('''you arrived at the island unharmed. there is a house with 3 doors . one is red,one is yellow,one is blue.which colour will u choose?''').lower()
      if choise3=="red":
          print("u win and found the treasure")
      elif choise3=="yellow":
          print("u got a beast,game over")
      elif choise3=="blue":
          print("game over , u got dragon which killed u")
   else:
       print("jaya killed u")
else:
    print("you fell into the hole. game over")

