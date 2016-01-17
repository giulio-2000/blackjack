# Test the Deck Class

from deck import Deck

import random
random.seed(1)

print( "Empty Deck" )
d = Deck()
print( d )
print( "\n" )

print( "Populate the deck with 52 cards" )
d.populate()
print( d )
print( "\n" )

print( "Populate the deck with 104 cards" )
d.populate( 2 )
print( d )
print( "\n" )

if( d.isEmpty() ):
    print( "d is empty" )
else:
    print( "d is not empty" )
print( "\n" ) 

print( d.getCardFromTop() )
