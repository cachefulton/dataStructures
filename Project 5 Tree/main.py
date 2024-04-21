'''
Project: 5
Author: Cache Fulton
Course: CS2420
Date: 11/6/21

Description:

Lessons Learned:

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree.
    
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    punctuation = tuple(''';:'"\,<>./?!`()-[]}{@#$%^&*_~''')
    tree = BST()
    file = open("around-the-world-in-80-days-3.txt", 'r')
    for line in file:
        line = line.strip().split()
        for word in line:
            for letter in word:
                if letter in punctuation:
                    continue # don't add punctuation to tree
                else:
                    tree.add(Pair(letter)) # put all letters into our binary search tree
    return tree

def main():
    ''' Program kicks off here.
    '''
    my_tree = make_tree()

if __name__ == "__main__":
    main()