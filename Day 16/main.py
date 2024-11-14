# import turtle

# abdulaziz = turtle.Turtle()
# abdulaziz.color("blue")
# abdulaziz.shape("square")
# display = turtle.Screen()
# display.bgcolor("yellow")
# abdulaziz.turtlesize(1)
# abdulaziz.fd(120)
# abdulaziz.rt(150)
# abdulaziz.fd(150)
# abdulaziz.lt(150)
# turtle.begin_fill()
# abdulaziz.bk(120)

# abdulaziz.lt(150)

# abdulaziz.fd(150)

# abdulaziz.rt(150)

# abdulaziz.fd(250)
# turtle.end_fill()





# turtle.done()
from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["names of pokimons","Types","Discription"]
table.add_row (["Flarexin","Fire","A fox-like Pakimon with fiery fur that can launch fireballs from its tail."])
table.add_row(["Aquaflume","Water","A fish Pakimon with fins that spray water to protect itself, skilled in underwater"])
table.add_row(["Terratuff","Rock / Ground","A sturdy turtle with rocky skin that can dig underground and cause minor"])
table.add_row(["Zephyron","Flying / Electric","An eagle Pakimon with electric wings that can control gusts of wind and thunder."])
table.align = "r"
print(table)