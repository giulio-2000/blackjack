# Test the Deck Class

from deck import Deck

import random
random.seed(1)

print( "Empty Deck" )
d = Deck()
print( d )
print( "\n" )

print( "Populate the deck with 52 cards" )
d.Populate()
print( d )
print( "\n" )

print( "Populate the deck with 104 cards" )
d.Populate( 2 )
print( d )
print( "\n" )

if( d.IsEmpty() ):
    print( "d is empty" )
else:
    print( "d is not empty" )
print( "\n" ) 

print( d.GetCardFromTop() )
