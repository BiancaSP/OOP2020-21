# course: Object-oriented programming, year 2, semester 1
# academic year: 2020-21
# author: B. Schoen-Phelan
# date: 13-11-2020
# purpose: Lab wk8 - Word Games

# base class
class WordGames:
    """
    Class to represent the word game's base class.
    Methods and attributes that every type of word
    game should have are defined here.
    ...
    Attributes:
    -----------
        __my_words : str
        Read from user input and identifies the word
        or sentence that a user has inputted.

    Methods:
    --------
        the_words:
            Property getter method that returns
            the value of the user inputted word
            or sentence

        word_play:
            Contains logic for playing the game.
            Child classes should override this
            method in order to implement their own
            game logic.
    """
    def __init__(self):
        """
        Constructs the necessary attributes for the
        WordGame object.

        Parameters: None.
        -----------

        Instance variables:
        -------------------
            __my_words : str
                Variable that holds the user inputted word or
                sentence. Set to enforced encapsulation via
                name mangling.
        """
        self.__my_words = input("Please enter a word or sentence: ")

    @property
    def the_words(self):
        """
        Property method to return the value of the user
        inputted word or sentence.

        Parameters: None.
        -----------

        Returns:
        ________
            __my_words : str
                The value of the word or sentence that has
                been inputted by a user.
        """
        return self.__my_words

    def word_play(self):
        """
        Plays the game. The base class version of playing
        the game simply prints the value that has been
        inputted.

        Parameters: None.
        -----------

        Returns: None.
        --------
        """
        print("User input was: "+self.the_words)

class WordDuplication(WordGames): # you implement this and provide docstrings
    pass

class WordScramble(WordGames): # you implement this and provide docstrings
    pass


# prints the docstrings info
# if this class was a python module
print(WordGames.__doc__)

# Create an instances of the classes here:
wg = WordGames()
wg.word_play()

