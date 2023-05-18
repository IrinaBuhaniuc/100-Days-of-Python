#import another_module

#print(another_module.another_variable)
#import turtle

#from turtle import Turtle, Screen
#annie = Turtle()
#annie.shape("turtle")
#annie.color("red")
#annie.forward(100)
#annie.backward(300)
#annie.left(90)
#annie.forward(100)
#annie.home()
#print(annie)


#my_screen = Screen()
#print(my_screen.canvheight)

#my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtie", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "r"
print(table)
