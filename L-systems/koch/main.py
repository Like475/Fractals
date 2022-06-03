import turtle

turtle.Screen().setup(1200, 600, 50, 50)
t = turtle.Turtle()
t.ht()
t.speed(0)

def draw(ln):
    if ln > 12:
        ln3 = ln // 3
        draw(ln3)
        t.lt(60)
        draw(ln3)
        t.rt(120)
        draw(ln3)
        t.lt(60)
        draw(ln3)
    else:
        t.fd(ln)
        t.lt(60)
        t.fd(ln)
        t.rt(120)
        t.fd(ln)
        t.lt(60)
        t.fd(ln)

draw(100)
t.rt(120)
draw(100)
t.rt(120)
draw(100)

turtle.done()