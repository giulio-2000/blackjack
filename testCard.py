# Test the Card class

from card import Card

import random
random.seed(1)

c = Card( "2", "C" )

print( c )

c.turnFaceDown()
c.turnFaceDown()

print( c )

c.turnFaceUp()

print( c )

c.flip()

print( c )

print( c.rank )
print( c.suit )

