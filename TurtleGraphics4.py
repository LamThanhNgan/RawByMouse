import turtle, random 
from turtle import Turtle, Screen
Colors = ['black','yellow','pink','green','blue','gray','purple','orange', 'lightyellow']
flat = False
screen = Screen()
t = turtle.Turtle("circle")
t.width(2)
def dragging(x,y):
	t.ondrag(None)
	t.setheading(t.towards(x, y))
	t.goto(x,y)
	t.ondrag(dragging)
def click_double_left(x,y):
	t.color(random.choice(Colors))
def clickright(x,y):
	t.clear()
def click_u_up() :
	t.penup()
def click_d_down():
	t.pendown()


turtle.listen()
t.ondrag(dragging)
turtle.onscreenclick(clickright,3)
turtle.onscreenclick(click_double_left,2)
turtle.onkey(click_u_up,'0')
turtle.onkey(click_d_down,'1') 
screen.mainloop()



