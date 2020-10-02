# @Author: Arshad Shah
# @Date:   Friday, October 2, 2020 9:15 AM
# @Email:  C19485866@mytudublin.ie
# @Filename: lab2.py
# @Last modified by:   Arshad Shah
# @Last modified time: Friday, October 2, 2020 10:58 AM



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

        # print only first and last of the sentence:
        print("first letter is %c and last letter is %c." % (message[0], message[-1]))

        # use slice notation:
        print("All letter reversed %s." % (message[::-1]))

        # escaping a character:
        print("He said \"that's fantastic\" !")

        # find all a's in the input word and count how many there are:
        str = message#for printing a
        a1 = message#for finding a
        find_a1 = str.find("a")#find a
        count_a = str.count('a')#count a
        print("letter a is first found on: " , find_a1)#print place number
        print("The count of a in the noun is: ",count_a)#print count of a
        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():



    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        list_1 = message.split()
        print(list_1)

        # append a new element to the list and print:
        list_1.append("very")
        print(list_1)

        # remove from the list in 3 ways:
        #method 1
        element = list_1.pop()
        print(element)
        print(list_1)

        #method 2
        list_1.remove("bad")#test sentence is bad fox as remove needs the element in list
        print(list_1)

        #method3
        del list_1[0]
        print(list_1)

        # check if the word cake is in your input list:


        # reverse the items in the list and print:


        # reverse the list with the slicing trick:


        # print the list 3 times by using multiplication:
        print(list_1*3)


tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()
