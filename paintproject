import turtle
turtle.ht()
turtle.speed(0)
print("welcome to the paint progaram,")
print("when you will click on the screen, a shape will appear.")
print("to change the shape press on --->")
print("Up - Circle, Down - Square, Left - Triangle, Right - Turtle.")
print("to change the color of the shape press on --->")
print("B - Blue, R - Red, G - Green, Y - Yellow.")
print("to change the size of the shape press on --->")
print("size 1 - 1, size 2 - 2, size 3 - 3, size 4 - 4.")
print("ENJOY!")

def size_1():    
    turtle.shapesize(1,1,1)
    
turtle.getscreen().onkeypress(size_1,"1")
turtle.getscreen().listen()

def size_2():    
    turtle.shapesize(2,2,2)
    
turtle.getscreen().onkeypress(size_2,"2")
turtle.getscreen().listen()


def size_4():    
    turtle.shapesize(4,4,4)
    
turtle.getscreen().onkeypress(size_4,"4")
turtle.getscreen().listen()
def size_3():    
    turtle.shapesize(3,3,3)
    
turtle.getscreen().onkeypress(size_3,"3")
turtle.getscreen().listen()

def turtle_shape():    
    turtle.shape("turtle")
    
turtle.getscreen().onkeypress(turtle_shape,"Right")
turtle.getscreen().listen()

def triangle_shape():    
    turtle.shape("triangle")
    
turtle.getscreen().onkeypress(triangle_shape,"Left")
turtle.getscreen().listen()

def circle_shape():    
    turtle.shape("circle")
    
turtle.getscreen().onkeypress(circle_shape,"Up")
turtle.getscreen().listen()

def square_shape():    
    turtle.shape("square")
    
turtle.getscreen().onkeypress(square_shape,"Down")
turtle.getscreen().listen()


def blue_color():    
    turtle.color("blue")
    
turtle.getscreen().onkeypress(blue_color,"b")
turtle.getscreen().listen()

def red_color():    
    turtle.color("red")
    
turtle.getscreen().onkeypress(red_color,"r")
turtle.getscreen().listen()

def green_color():    
    turtle.color("green")
    
turtle.getscreen().onkeypress(green_color,"g")
turtle.getscreen().listen()

def yellow_color():    
    turtle.color("yellow")
    
turtle.getscreen().onkeypress(yellow_color,"y")
turtle.getscreen().listen()

turtle.color("blue")
turtle.shape("circle")

def stamp(x,y):
    turtle.ht()
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.stamp()

turtle.onscreenclick(stamp, btn=1, add=True)


turtle.mainloop()
