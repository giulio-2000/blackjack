# Test the Deck Class

from card import Card
from deck import Deck

import random
random.seed(1)

d = Deck()

c = Card( "3", "S" )

d.addToTop( c )
d.addToTop( Card( "3", "S" ) )

print( "The deck is now:" )
print( d )
print( "\n" )

print( "Add AH card to bottom:" )
d.addToBottom( Card( "A", "H" ) )
print( d )
print( "\n" )

print( "Shuffle the deck:" )
d.shuffle()
print( d )

d2 = Deck()
d2.addToTop( Card( "2", "C" ) )
d2.addToTop( Card( "3", "C" ) )
d2.addToTop( Card( "4", "C" ) )
d2.addToTop( Card( "5", "C" ) )
d2.addToTop( Card( "6", "C" ) )

print( "Add clubs mini deck to bottom:" )
d.addToBottom( d2 )
print( d )
print( "\n" )

print( "Add clubs mini deck to top:" )
d.addToTop( d2 )
print( d )
print( "\n" )

print( "Remove one card from top:" )
d.removeFromTop( )
print( d )
print( "\n" )


print( "Remove five more cards from top:" )
d.removeFromTop( 5 )
print( d )
print( "\n" )

