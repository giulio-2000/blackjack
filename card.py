# Class to represent a French Card

# Has two properties: Rank and Suit
# By default, it displays like, e.g., 8H, 
# but it can be turned face down in which case it displays like XX

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
            raise Exception( "Invalid rank!" )
        if( suit not in Card.SUITS ):
            raise Exception( "Invalid suit!" )
        self.__rank       = rank
        self.__suit       = suit
        self.__isFaceDown = isFaceDown
    
    def __str__( self ):
        rep = ""
        if( self.__isFaceDown ):
            rep = "XX"
        else:
            rep = self.__rank + self.__suit
        return rep
    
    @property
    def Rank( self ):
        return self.__rank
    
    @property
    def Suit( self ):
        return self.__suit

    # If is faceDown, turn it face up and vice-versa
    def Flip( self ):
        self.__isFaceDown = not self.__isFaceDown
    
    # Turns the card face up
    def TurnFaceUp( self ):
        self.__isFaceDown = False
    
    # Turns the card face down
    def TurnFaceDown( self ):
        self.__isFaceDown = True



if( __name__ == "__main__" ):
    print("It is not allowed to run this module directly! Pls import it!")
    input("\n\nPress the enter key to exit.")
