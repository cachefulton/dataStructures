class Stack:
    def __init__(self):
        self.my_stack = []

    def push(self, item):
        '''Push an item onto the stack. Size increases by 1.'''
        self.my_stack.append(item)
        return

    def pop(self):
        '''Remove the top item from the stack and return it. 
        Raise an IndexError if the stack is empty.
        '''
        return self.my_stack.pop()

    def top(self):
        '''Return the item on top of the stack without removing it. 
        Raise an IndexError if the stack is empty.
        '''
        return self.my_stack[-1]

    def size(self):
        '''Return the number of items on the stack.'''
        return len(self.my_stack)

    def clear(self):
        '''Empty the stack.'''
        self.my_stack = []
        return 
    