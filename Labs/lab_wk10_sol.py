# Object Oriented Programming
# Semester 1: Python
# Academic year 2020-21
# Lab Week 10
# Abstract Classes
# author: B. Schoen-Phelan
# date: Nov 2020

# imports
from abc import ABC, abstractmethod


# Abstract base class definition
class MathsGame(ABC):
    """
    The abstract base class that defines the scaffold of
    how to play a maths game for children.
    ...
    Attributes:
    -----------
        user_input_property : abstract property
            Getter method to control access to user input
            type to be decided by derived class(es).

    Methods:
    --------
        __init__ : abstract method
            Prints out a welcome message.

        play_game : abstract method
            Provides the game play.
            Logic to be implemented by the derived class(es).
    """

    @abstractmethod
    def __init__(self):
        """
        Currently sets a welcome message.
        Any instance variables necessary for game play should
        be declared here.
        Derived classes must implement this abstract method.
        """
        print("Welcome to the Math Game")

    @property
    @abstractmethod
    def user_input_property(self):
        """
        Abstract method.
        To be a property to control access to the user input.
        If a setter method is necessary for the specific game
        to play, please implement this in the derived class(es).
        """
        pass

    @abstractmethod  # using the decorator
    def play_game(self):
        """
        Abstract method.
        Access method to start the playing of a game.
        """
        pass


# class Fibonacci will be inherited from Maths Game.
class FibonacciGame(MathsGame):
    """
    Class derived from the MathsGame abstract class.
    FibonacciGame provides a game that prints a certain
    number of terms in the Fibonacci sequence. Then the
    user is asked for the next number. This game can be
    played endlessly. After finishing the game play there
    will be output in how many games the next in the
    sequence was guessed correctly.

    Attributes:
    -----------
        self.__input : int
            Holds the user input.

    Methods:
    --------
        __init__(self)
            Sets the input variable to 0
            Also calls parent class's init

        user_input_property : property
            Getter returns the value of the instance
            variable self.__input
            Setter sets the value of the instance
            variable self.__input

        play_game(self)
            Returns : none
            Handles the game playing logic. Makes a
            call to the calculate_fibonacci static
            method

        calculate_fibonacci(terms)
            Calculates the Fibonacci sequence for a given
            number of terms.
            Argument: takes the number of terms to play
            Returns: list that holds the amount of
                Fibonacci terms
            Raises:
                TypeError if terms is not of type int
                ValueError if terms is 0 or below
    """

    def __init__(self):
        """
        Initialisation class. Calls the base classe's
        welcome message. Sets an instance variable
        called self.__input to
        receive the user input. Start content is 0.
        """
        super().__init__()
        self.__input = 0

    @property
    def user_input_property(self):
        """
        Getter method to return the value of the instance
        variable self.__input.
        """
        return self.__input

    @user_input_property.setter
    def user_input_property(self, value):
        """
        Setter method to set user input in self.__input
        to a specific value. Currently no validation check.
        """
        self.__input = value

    def play_game(self):
        """
        Implementation of the abstract method play_game.
        Attributes: none
        returns: none
        """
        right_guesses = 0
        keep_playing = True

        # while True allows us to play the game as many times as we wish
        while keep_playing:
            try:
                self.user_input_property = int(input("Enter 1 to play, Enter 2 to exit: "))
                if self.user_input_property not in range(1, 3):
                    print("Wrong input. Allowed are 1 to play or 2 to exit.")
            except:
                print("Enter a whole number: either 1 or 2")
                continue

            # we want to play is option 1
            if self.user_input_property == 1:
                try:
                    terms = int(input("How many terms: "))

                    if terms != 0:
                        # we want it to calculate one extra because we want to
                        # check that the user understood the sequence so we
                        # need the next number even if we won't display it
                        fibs = self.calculate_fibonacci(terms + 1)

                        # displaying all but the last one
                        # remember: slicing always EXCLUDES the element at the
                        # end position
                        print(fibs[:-1])

                        right_or_wrong = int(input("Guess the next number: "))
                        if right_or_wrong == fibs[-1]:
                            print("Well done")
                            right_guesses += 1
                        else:
                            print("sorry, this was wrong.\n The right number is: ", fibs[-1])

                    else:  # means we don't want to return anything
                        print("Nothing to play.")
                except:
                    # this currently jumps back to the decision if play or not play
                    print("Terms must be a whole number.")

            elif self.user_input_property == 2:
                # this message will currently be printed even if the
                # user never played a game.
                print(f"You got {right_guesses} right this game!")

                # setting keep_playing to false forces the loop to not
                # run anymore
                keep_playing = False

    # this method is a good candidate for a static method
    # all it does is to calculate the Fibonacci number,
    # which is independent of the game. Might be nice to
    # offer the functionality to other games.
    @staticmethod
    def calculate_fibonacci(terms):
        """
        Static method to calculate the Fibonacci sequence.
        ...
        Arguments:
        ----------
            terms : int
                A whole number to indicate how many terms in the
                Fibonacci sequence should be displayed.
                If a non-int term is entered a TypeError is thrown.
                If a number smaller equal 0 is entered a
                ValueError is thrown.

        Returns:
        --------
            fib_numbers : list
                Holds the fibonacci numbers. The amount of terms
                depends on what is specified in the received
                argument.
        Raises:
        -------
            TypeError if the function argument is not of type int.
            ValueError if the function argument is zero or below.
        """
        # as part of our game structure, this is already
        # caught at the level of user error.
        # But as this is a static method, it should be
        # able to act independently and catch these issues.
        if type(terms) is not int:
            raise TypeError("Fibonacci terms need to be a whole number greater than zero.")

        # list that holds the fibonacci numbers
        fib_numbers = []

        # really only worth computing if we have
        # more than 1 in the terms
        if terms > 1:
            fib_numbers.extend([0, 1])

            before_before = 0
            before = 1

            # we start the for loop at index 2 in the list
            # and go up to term-1 as range excludes the last.
            # We already have two
            # numbers in our fibonacci list, so if the term
            # is 3, 3 -2 already entered numbers means we need
            # 1 additional number. We start at index 2 and end at 2, so 1
            # number will be added to the sequence. If the
            # term is 5, then -2 existing numbers means we
            # need 3 additional numbers: index 2, 3 and 4.
            for number in range(2, terms):
                # actual calculation
                current = before_before + before
                fib_numbers.append(current)

                # now fix variables for next run
                before_before = before
                before = current

        elif terms == 1:
            fib_numbers.append(0)
        elif terms <= 0:
            # as part of our game structure this case would not
            # happen, as 0 is caught already in the options above.
            # However, if this was used as a static method it should
            # have self-contained validation.
            raise ValueError("Cannot do Fibonacci for 0 terms")

        return fib_numbers


# Object instantiation
f = FibonacciGame()
f.play_game()

# display fibonacci terms using the static method
# try:
#     print(FibonacciGame.calculate_fibonacci(10))
# except Exception as e:
#     print(e)
