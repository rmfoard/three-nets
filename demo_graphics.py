from graphics import *

def main():
    win = GraphWin("My Circle", 200, 200)
    c = Circle(Point(100, 100), 10)
    c.draw(win)
    win.getMouse()
    win.close()

main()
