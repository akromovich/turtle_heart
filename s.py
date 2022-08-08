from turtle import *
setup(800,800)
bgcolor("black")
color("red")
speed(5)
pencolor("black")
begin_fill()
for n in range(2):
    rt(90)
    fd(300)
    rt(90)
    fd(40)

end_fill()
up()
goto(150,0)
down()
begin_fill()
for i in range(2):
    fd(40)
    rt(90)
    fd(300)
    rt(90)
end_fill()
up()
goto(-40,0)
down()
begin_fill()
rt(58)
fd(355)
lt(58)
fd(43)
lt(122)
fd(355)
lt(58)
fd(43)

end_fill()
hideturtle()



exitonclick()
mainloop()