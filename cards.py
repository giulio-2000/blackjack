
# The French Playing Card Class
class Card( object ):

    RANKS = ( "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", 
                 "J", "Q", "K"  )

    SUITS = ( "C", "D", "H", "S" )

    # Init from two strings and, optionally, a boolean
    def __init__( self, rank, suit, isFaceDown = False ):
        if( type(rank) != str ):
            raise Exception( "rank should be a string" )
        if( type(rank) != str ):
            raise Exception( "suit should be a string" )
        rank = rank.upper()
        suit = suit.upper()
        if( rank not in Card.RANKS ):
            raise Exception( "invalid rank" )
        if( suit not in Card.SUITS ):
            raise Exception( "invalid suit" )
        self.__rank       = rank
        self.__suit       = suit
        self.__isFaceDown = isFaceDown
    
    @property
    def Rank( self ):
        return self.__rank
    
    @property
    def Suit( self ):
        return self.__suit
    
    def __str__( self ):
        rep = ""
        if( self.__isFaceDown ):
            rep = "XX"
        else:
            rep = self.__rank + self.__suit
        return rep
    
    def Flip( self ):
        self.__isFaceDown = not self.__isFaceDown
        
    def TurnFaceUp( self ):
        self.__isFaceDown = False
        
    def TurnFaceDown( self ):
        self.__isFaceDown = True


        
# Class to represent a deck of French Cards
# This deck might be empty or populated with an arbitrary amount of cards
# Cards might be repeated.
# TODO: make this class iterable
class Deck( object ):
    
    def __init__( self ):
        self.__cards = []
    
    def __str__( self ):
        rep = ""
        if( self.IsEmpty() ):
            rep = "<emptyDeck>"
        else:
            for c in self.__cards:
                rep += c.__str__() + "\n"
        return rep
    
    # Clears and populate with [numStdDecks] std Freach card decks
    # Does not shuffle
    def Populate( self, numStdDecks = 1 ):
        self.Clear()
        for n in range( numStdDecks ):
            for s in Card.SUITS:
                for r in Card.RANKS:
                    c = Card( r, s )
                    self.__cards.append( c )
    
    # Checks if the deck is empty
    def IsEmpty( self ):
        return ( not self.__cards )
    
    # Clears the deck
    def Clear( self ):
        self.__cards = []
    
    # Shuffles the deck    
    def Shuffle( self ):
        from random import shuffle
        shuffle( self.__cards )
    
    # Get the card from the top (but does not remove it from the deck)
    # If the deck is empty, throws an error 
    # TODO: maybe avoid error in the latter case and return a "default" theCard
    def GetCardFromTop( self ):
        if( self.IsEmpty ):
            raise Exception( "Cannot GetCardFromTop if the deck is empty" )
        return self.__cards[0]
    
    # Adds a card/deck to the top
    def AddToTop( self, toBeAdded ):
        if( type( toBeAdded ) == Card ):
            self.__cards.insert( 0, toBeAdded )
        elif( type( toBeAdded ) == Deck ):
            for c in reversed( toBeAdded.__cards ):
                self.__cards.insert( 0, c )
        else:
            raise Exception( "AddToTop only takes cards or decks" )
            
    # Adds a card/deck to the bottom
    def AddToBottom( self, toBeAdded ):
        if( type( toBeAdded ) == Card ):
            self.__cards.append( toBeAdded )
        elif( type( toBeAdded ) == Deck ):
            for c in toBeAdded.__cards:
                self.__cards.append( c )
        else:
            raise Exception( "AddToBottom only takes cards or decks" )
    
    # Removes [numToRemove] cards from the top of the deck
    # If [numToRemove] is >= than size of the deck, this is equivalent to clearing the deck
    def RemoveFromTop( self, numToRemove = 1 ):
        if( numToRemove < 0 ):
            raise Exception( "RemoveFromTop: numToRemove cannot be negative " )
        if( self.__cards ):
            del self.__cards[0:numToRemove]
    
            
            
someDeck = Deck()
someDeck.AddToTop( Card( "A", "H" ) )
someDeck.AddToTop( Card( "2", "H" ) )
someDeck.AddToTop( Card( "3", "H" ) )
print( someDeck )

d = Deck()
d.AddToTop( someDeck )
d.AddToBottom( someDeck )
print( d )
