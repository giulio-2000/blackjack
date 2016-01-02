from card import Card
from deck import Deck


someDeck = Deck()

someDeck.AddToTop( Card( "A", "H" ) )
someDeck.AddToTop( Card( "2", "H" ) )
someDeck.AddToTop( Card( "3", "H" ) )

print( someDeck )

d = Deck()
d.AddToTop( someDeck )
d.AddToBottom( someDeck )

print( d )

