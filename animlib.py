import time
from graphics import *
window = GraphWin("cope", 800, 600)
def getPos(element):
    thing = type(element)
    if thing in [Circle, Rectangle, Oval]:
        return element.getCenter()
    elif thing == Point:
        return element
    elif thing == Image:
        return elemnt.getAnchor()
    else:
        accX = 0
        accY = 0
        points = element.getPoints()
        for i in points:
            accX += i.x
            accY += i.y

        return Point(accX / len(points), accY / len(points))
    
def TweenElement(element, point, speed):
    initialPos = getPos(element)
    moveX = point.x - initialPos.x
    moveY = point.y - initialPos.y

    iTime = time.time()
    delta = iTime
    elapsed = iTime

    while time.time() - iTime <= speed:
        elapsed = time.time() - delta
        delta = time.time()
        element.move(elapsed * moveX / speed, elapsed * moveY / speed)

    currentPos = getPos(element)
    element.move(point.x - currentPos.x, point.y - currentPos.y)

cir = Circle(Point(100, 100), 10)
cir.draw(window)
TweenElement(cir, Point(700, 100), 0.1)
