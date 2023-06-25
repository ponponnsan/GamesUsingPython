from turtle import *
shape('turtle')

setup(600, 600)
color('cyan')
Screen().bgcolor('navy')
width(3)
speed(10)

def drawline(data):
    for i in range(len(data)):
        if i ==0:
            penup()
        goto(data[i][0], data[i][1])
        pendown()
   
drawline([[100, 100],[100,0]])
drawline([[-100, 100],[-100,0]])
drawline([[100, -100],[-100,-100]])

drawline([[200, 200],[-200,200],[-200, -200], [200, -200], [200, 200]])
done()

