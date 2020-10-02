# Object oriented programming
# semester 1: Python
# Dr Bianca Schoen-Phelan
# Sep 2020
# Code for Lab 1: first steps
# task: run this code, play with it,
# do you understand what happens?
from self import self


class FirstLab:
    def __init__(self):
        print("hi, this is my first python class")

    def sec(self):
        print("I can print anywhere I like")


# noinspection PyMethodMayBeStatic
class MyClass:
    @staticmethod
    def SayHello():
        print("Hello there!")


MyClass.SayHello()
fl = FirstLab()


# uncomment the following line, play with it
