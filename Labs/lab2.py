#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        #
        # Enter your own print statements below:
        #

        # print only first and last of the sentence:


        # use slice notation:


        # escaping a character:


        # find all a's in the input word and count how many there are:


        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:


        # append a new element to the list and print:


        # remove from the list in 3 ways:


        # check if the word cake is in your input list:


        # reverse the items in the list and print:


        # reverse the list with the slicing trick:


        # print the list 3 times by using multiplication:



tas = Types_and_Strings()
tas.play_with_strings()
#tas.play_with_lists()
