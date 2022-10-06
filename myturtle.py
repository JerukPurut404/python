import turtle as t 
t.setup

def driehoek():
    
    t.color("pink")

for x in range(3):
    
    t.color("pink") #Invisible Triangle 
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100) 

    t.penup()
    t.right(150)
    t.forward(50)

    t.color("blue") #Upside down Triangle 
    t.pendown()
    t.right(90)
    t.forward(100)
    t.left(120)
    t.left(90)
    t.left(30)
    t.forward(100)

    t.left(120)
    t.left(90)
    t.left(30)
    t.forward(100)
    t.left(90)
    t.left(90)
    t.left(30)
    t.left(30)
    t.forward(100)


driehoek()
input()
