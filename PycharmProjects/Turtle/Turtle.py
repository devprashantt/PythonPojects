# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# my_screen = Screen()
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Prashant","Jaya"])
table.add_column("Type",["Electric","Boy","Girl"])
table.align = "l"
print(table)

