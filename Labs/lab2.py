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
        print("Hello how are you?")

        # print only first and last of the sentence:
        print(message[0])#first
        print(message[-1])#last

        # use slice notation:
        print(message[3:]) #print from third to last position

        print(message[1:5])#print from first to fifth position

        print(message[:])#print everything using slice notation



        # escaping a character:
        print("He said \"that\'s fantastic\" !")

        # find all a's in the input word and count how many there are:
        lower_case = message.lower()
        print(lower_case)
        print("The first occurence of a is at position: " + str(lower_case.find('a')))
        print("There are " + str(lower_case.count('a')) + " a's in the word.")
        print("Total character count is: " + str(len(lower_case)))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():
        print(lower_case.replace('a', '_'))


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:
        list_message = message.split(" ")

        print(list_message)

        # append a new element to the list and print:
        list_message.append('good')

        print(list_message)

        # remove from the list in 3 ways:
        #pop method
        list_message.pop(0)
        print(list_message)

        #del
        del list_message[-1:-3]
        print(list_message)

        #remove
        list_message.remove('good')
        print(list_message)

        # check if the word cake is in your input list:
        print('cake' in list_message)

        # reverse the items in the list and print:
        list_message.reverse()
        print(list_message)

        # reverse the list with the slicing trick:
        list_message[::-1]
        print(list_message)

        # print the list 3 times by using multiplication:
        print(list_message * 3)


tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()
