#!/usr/bin/python3
""" MyList Class
    it module that creates a class MyList that inherits from list
"""


class MyList(list):
    """function that defines a class mylist
    """
    def print_sorted(self):
        print(sorted(self))
