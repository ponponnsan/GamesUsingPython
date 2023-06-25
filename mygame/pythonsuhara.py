from turtle import *
shape('turtle')
setup(450, 450)
color('orange')
Screen().bgcolor('blueviolet')
width(5)
speed(10)

def drawline(data):
    for i in range(len(data)):
        if i ==0:
            penup()
        goto(data[i][0],data[i][1])
        pendown()


def ballon(x, y):
    penup()
    setposition(x, y)
    pendown()
    circle(50)

    
drawline([[-350, 220],[-250,220],[-350, 100]])
drawline([[-290, 170],[-240,100]])

drawline([[-50, 200],[-100,100]])
drawline([[50, 200],[100,100]])

drawline([[250, 220],[300,220]])
drawline([[230, 190],[320,190], [270, 100]])

drawline([[-230, -130],[-150,-130],[-150, -210]])
drawline([[-285, -210],[-80,-210]])

drawline([[100, -130],[180,-130],[180, -230], [150, -230]])
drawline([[120, -100],[110,-230]])


    
for i in range(5):
    ballon(400,-200)
    right(360/5)


ht()
done()

             
