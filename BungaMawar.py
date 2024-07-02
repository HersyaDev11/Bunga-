import turtle

turtle.bgcolor('black')
turtle.speed(20)
turtle.hideturtle()

colors = ["blue","salmon","purple","green"]

for i in range(120):
    for c in colors:
        turtle.color(c)
        turtle.circle(180-i,100)
        turtle.lt(90)
        turtle.circle(180-i,100)
        turtle.end_fill()
turtle.mainloop()       
    
