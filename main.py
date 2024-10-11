# L. Louque
# 1/12/2023-1/16/2023
# rubberDuck

import turtle

t = turtle.Turtle()

def drawBody():
  t.up()
  t.begin_fill()
  #Bottom
  t.setpos(xValue,yValue)
  t.seth(-100)
  t.color(outline)
  t.fillcolor(duckColor)
  t.down()
  t.circle(200,215)
  #Tail
  t.circle(30,150)
  #Back
  t.seth(220)
  t.circle(-130,80)
  #Head
  t.seth(60)
  t.circle(100,260)
  t.setpos(xValue,yValue)
  t.end_fill()
def drawWing():
  t.up()
  t.color(outline)
  #Wing
  t.setpos(xValue+150,yValue-30)
  t.seth(25)
  t.down()
  t.circle(-150,60)
  t.circle(-40,100)
  t.circle(-150,70)
  t.up()
  #Bottom Feather
  t.setpos(xValue+310,yValue-95)
  t.down()
  t.seth(200)
  t.circle(-170,25)
  t.up()
  #Middle Feather
  t.setpos(xValue+315,yValue-72)
  t.down()
  t.seth(200)
  t.circle(-170,25)
  t.up()
  #Top Feather
  t.setpos(xValue+305,yValue-49)
  t.down()
  t.seth(200)
  t.circle(-170,25)
def drawBeak():
  t.up()
  t.color(outline)
  t.begin_fill()
  #Top
  t.setpos(xValue+30,yValue+95)
  t.seth(-135)
  t.down()
  t.circle(-70,60)
  #Tip
  t.circle(15,145)
  #Bottom
  t.circle(100,60)
  t.color(beakColor)
  t.setpos(xValue+30,yValue+95)
  t.end_fill()
  t.up()
  #Beak Opening
  t.setpos(xValue-38,yValue+40)
  t.seth(0)
  t.color(outline)
  t.down()
  t.setpos(xValue-15,yValue+40)
  t.circle(15,60)
def drawEye():
  #Whites
    #Right
  t.up()
  t.setpos(xValue+70,yValue+90)
  t.seth(0)
  t.begin_fill()
  t.color("white")
  t.down()
  t.circle(30)
  t.end_fill()
    #Left
  t.up()
  t.setpos(xValue-10,yValue+90)
  t.begin_fill()
  t.color("white")
  t.down()
  t.circle(30)
  t.end_fill()
  #Pupils
    #Right
  t.up()
  t.setpos(xValue+65,yValue+100)
  t.seth(0)
  t.begin_fill()
  t.color("black")
  t.down()
  t.circle(18)
  t.end_fill()
    #Left
  t.up()
  t.setpos(xValue-5,yValue+100)
  t.seth(0)
  t.begin_fill()
  t.color("black")
  t.down()
  t.circle(18)
  t.end_fill()
def drawWords():
  t.up()
  t.setpos(xValue-315,yValue+225)
  t.seth(-90)
  t.color(boxBackground)
  t.begin_fill()
  t.down()
  for x in range(0,2):
    t.forward(50)
    t.left(90)
    t.forward(300)
    t.left(90)
  t.end_fill()
  t.color(textColor)
  t.up()
  t.setpos(xValue-300,yValue+200)
  t.write("def adding(num1,num2):",font=Style)
  t.setpos(xValue-275,yValue+175)
  t.write("return num1 + num2",font=Style)
t.ht()
t.speed(0)

xValue = -75
yValue = 0

outline = "darkOrange"
duckColor = "yellow"
beakColor = "gold"
boxBackground = "cadetBlue1"
textColor = "black"

Style = ("Courier",15)

drawBody()
drawWing()
drawBeak()
drawEye()
drawWords()