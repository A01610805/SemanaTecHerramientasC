"""Tic Tac Toe

Retrieved from https://grantjenks.com/docs/freegames/tictactoe.html
                                                    on 15/09/2020
Modified by Rodrigo Muñoz Guerrero on 15/09/2020
"""

from turtle import (color, up, goto, down, circle, update, setup,
                    hideturtle, tracer, onscreenclick, done)
from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('blue')
    line(x+32, y+32, x + 101, y + 101)
    line(x+32, y + 101, x + 101, y+32)


def drawo(x, y):
    """Draw O player."""
    color('red')
    up()
    goto(x + 67, y + 25)
    down()
    circle(42)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    if y not in yd:         # Create the index if it is not in the dictionary
        yd[y] = []
    if x not in xd:         # Create the index if it is not in the dictionary
        xd[x] = []
    if x in yd[y] and y in xd[x]:       # Checks if the box is empty
        print("Casilla ocupada")
    else:
        xd[x].append(y)
        yd[y].append(x)
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player


xd = {}
yd = {}
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
