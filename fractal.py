#Draw a fractal tree
import turtle
import random

def tree(branchLen,t):
    if branchLen < 10:
        t.color("green")
    if branchLen > 5:
        t.forward(branchLen)
        t.right(random.randint(15,45))
        tree(branchLen-random.randint(10,20),t)
        t.left(random.randint(15,45))
        tree(branchLen-random.randint(10,20),t)
        t.right(random.randint(15,45))
        t.backward(branchLen)
    if branchLen >= 10:
        t.color("black")
def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    #pull the pin up
    t.up()
    t.backward(100)
    #put the pin down
    t.down()
    #change the color
    t.color("black")
    tree(75,t)
    myWin.exitonclick()

main()

