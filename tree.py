import turtle
u= turtle.Turtle()
u.screen.bgcolor('sky blue')
u.pensize(4)
u.color('green')
u.left(90)
u.backward(100)
u.speed(200)
u.shape("turtle")

def tree(i):
    if i<10:
        return
    else:
        u.forward(i)
        u.color('red')
        u.circle(2)
        u.color('orange')
        u.left(30)
        tree(3*i/4)
        u.right(60)
        tree(3*i/4)
        u.left(30)
        u.backward(i)
tree(100)
turtle.done()

