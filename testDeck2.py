# Test the Deck Class

from card import Card
from deck import Deck


d = Deck()

c = Card( "3", "S" )

d.AddToTop( c )
d.AddToTop( Card( "3", "S" ) )

print( "The deck is now:" )
print( d )
print( "\n" )

print( "Add AH card to bottom:" )
d.AddToBottom( Card( "A", "H" ) )
print( d )
print( "\n" )

print( "Shuffle the deck:" )
d.Shuffle()
print( d )

d2 = Deck()
d2.AddToTop( Card( "2", "C" ) )
d2.AddToTop( Card( "3", "C" ) )
d2.AddToTop( Card( "4", "C" ) )
d2.AddToTop( Card( "5", "C" ) )
d2.AddToTop( Card( "6", "C" ) )

print( "Add clubs mini deck to bottom:" )
d.AddToBottom( d2 )
print( d )
print( "\n" )

print( "Add clubs mini deck to top:" )
d.AddToTop( d2 )
print( d )
print( "\n" )

print( "Remove one card from top:" )
d.RemoveFromTop( )
print( d )
print( "\n" )


print( "Remove five more cards from top:" )
d.RemoveFromTop( 5 )
print( d )
print( "\n" )

