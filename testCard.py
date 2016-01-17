# Test the Card class

from card import Card

import random
random.seed(1)

c = Card( "2", "C" )

print( c )

c.TurnFaceDown()
c.TurnFaceDown()

print( c )

c.TurnFaceUp()

print( c )

c.Flip()

print( c )

print( c.Rank )
print( c.Suit )

