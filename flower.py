from turtle import *

def fleur():
    for i in range(300):
        bgcolor('orange')
        circle(190-i, 90)
        left(90)
        circle(190-i, 90)
        left(18)
        speed(500)

fleur()
mainloop()
