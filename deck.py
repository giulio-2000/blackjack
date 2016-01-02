# Class to represent a deck of French Cards

# This deck might be empty or populated with an arbitrary amount of cards
# Note: Cards might be repeated!

# TODO:
# - make this class iterable

from card import Card


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



if( __name__ == "__main__" ):
    print("It is not allowed to run this module directly! Pls import it!")
    input("\n\nPress the enter key to exit.")
