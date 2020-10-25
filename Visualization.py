import turtle

def draw(turtle, height, degree, name, value):
    #draw multiple arrow according to the value
    additionalHeight = 25
    turtle.forward(height)

    not_debunked = value[0]
    debunked = value[1]
    debunked_count = 0
    for i in range(not_debunked):
        draw_arrow(turtle, additionalHeight)
        if(debunked_count < debunked):
            draw_circle(turtle, 10)
            debunked_count += 1

            
    #Lable text
    label(turtle, additionalHeight*3.2, name)
    
    #Go back to initial pos
    turtle.right(180)
    turtle.forward(height + additionalHeight*not_debunked)
    turtle.right(180)
    
    #Turn right after the draw to make a circle
    turtle.right(degree)

def draw_circle(turtle, size):
   turtle.penup()
   turtle.backward(size/2)
   turtle.right(90)
   turtle.forward(size)
   turtle.pendown()
   turtle.left(90)
   turtle.circle(size)

   turtle.penup()
   turtle.right(270)
   turtle.forward(size)
   turtle.right(90)
   turtle.forward(size/2)
   turtle.pendown()
   
   

def label(turtle, additionalHeight, name):
    turtle.penup()
    turtle.forward(additionalHeight)
    turtle.write(name, font=("Arial", 12, "bold"))
    turtle.right(180)
    turtle.forward(additionalHeight)
    turtle.right(180)
    turtle.pendown()

def draw_arrow(turtle, height):
    size = 20

    #Go to a certain height
    turtle.forward(height)
    
    #Left arrow
    turtle.left(150)
    turtle.forward(size)
    turtle.right(180)
    turtle.forward(size)
    turtle.left(30)

    #Right arrow  
    turtle.right(150)
    turtle.forward(size)
    turtle.right(180)
    turtle.forward(size)
    turtle.right(30)

    

    
def changeColor(r,g,b, r_start, r_end,
                g_start, g_end,
                b_start, b_end, totalLine):
    r+=(r_end-r_start)/totalLine
    g-=(g_start-g_end)/totalLine
    b+=(b_end-b_start)/totalLine
    return r,g,b

def drawGraph(category_dict):
    #Set up turtle, screen and turn the turtle to north direction
    t = turtle.Turtle()
    mw = turtle.Screen()
    mw.setup(width = 650, height = 650)
    t.hideturtle()
    t.speed(0)
    t.pensize(2)
    t.left(90)
    totalLine = len(category_dict)
    lineLength = 90
    #Color should be from 0 to 1 (0/255 to 255/255)
    r,g,b = 0.0,255/255,153/255
    for k,v in sorted(category_dict.items(),
                       key=lambda x:x[1]):
        tuples = (r,g,b)
        t.pencolor(tuples)
        draw(t, lineLength, 360/totalLine, k, v)
        r,g,b = changeColor(r,g,b,
                            0.0,0.0,
                            255/255,153/255,
                            153/255,204/255,
                            totalLine)
    legend(t)

    
def legend(turtle):
    turtle.pencolor('black')
    turtle.penup()
    turtle.goto(-170, -275)
    turtle.pendown()

    turtle.write("Notes: 1 arrow = 1 BS, 1 circle = 1 debunked BS",
                 font=("Arial", 12, "normal"))
 
