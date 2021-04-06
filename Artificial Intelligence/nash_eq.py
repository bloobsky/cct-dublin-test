# nash equilibrium with prissoner dillema

import nashpy
import numpy

Alan = numpy.array([[-1, -15], [0, -10]])
Ben = numpy.array([[-1, 0], [-15, -10]])

game = nashpy.Game(Alan, Ben)

equilibria = game.support_enumeration()
for eq in equilibria:
    print(eq)
    a = 0
    print(a)
    a += 1

# exercise3 . ai . co
Player1 = numpy.array([[4, -5], [-1, 0 ]])
Player2 = numpy.array([[2, 6], [5, -2]])

game2 = nashpy.Game(Player1, Player2)
game2

equ = game2.support_enumeration()
for e in equ:
    print(e)
