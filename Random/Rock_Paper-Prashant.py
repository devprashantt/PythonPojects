import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
diagram=[rock,paper,scissors]
user_choise=int(input("type 0 for rock,1 for paper,2 for scissors\n"))
computer_choise=random.randint(0,2)
print(diagram[computer_choise])
if user_choise>2:
    print("invalid")
else:
    print(diagram[user_choise])
    if user_choise==computer_choise:
        print("draw")
    elif user_choise==0 and computer_choise==2:
        print("you won")
    elif user_choise<computer_choise:
        print("you loose")
    elif user_choise>computer_choise:
        print("you won")
