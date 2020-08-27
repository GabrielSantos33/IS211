#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Gabriel Santos IS211
"""Assignment 1 part 2"""


class Book(object):
    """Create a class called Book. The class should have the following
    properties:
    a. Two attributes, author and title, both of which should be initialized
    to the blank string
    b. An __init__ function that takes in an author and a title, and sets them
    to the object variables
    c. A function called display, which when called, simply prints out a
    string representing the book. The output should be in the form of “title,
    written by author”. Example: “Of Mice and Men, written by John Steinbeck”
    ."""

    def __init__(self, author="", title=""):
        """a. Two attributes, author and title, both of which should be
        initialized to the blank string
        b. An __init__ function that takes in an author and a title,
        and sets them to the object variables"""

        self.author = author
        self.title = title

    def display(self):
        """c. A function called display, which when called, simply prints out
        a string representing the book. The output should be in the form
        of “title, written by author”. Example: “Of Mice and Men, written
        by John Steinbeck”."""

        return self.title +", written by " + self.author

Mice_Men = Book("John Steinbeck", "Of Mice and Men")
Mockingbird = Book("Harper Lee", "To Kill a Mockingbird")
print Mice_Men.display()
print Mockingbird.display()

