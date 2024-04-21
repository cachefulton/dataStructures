'''
This file will be able to create a linked list and manipulate it with help from course.py.
'''

class CourseList:
    def __init__(self):
        self.head = None

    def insert(self, course):
        '''insert the specified Course in Course Number ascending order'''
        new_course = course
        val_1 = None
        val_2 = self.head
        while val_2 != None and val_2.number() <= new_course.number():
            val_1 = val_2
            val_2 = val_2.next
        if val_1 == None:
            new_course.next = self.head
            self.head = new_course
        else:
            new_course.next = val_1.next
            val_1.next = new_course

    def remove(self, number):
        '''remove the first occurrence of the specified Course'''
        pointer = self.head
        pointer_2 = None
        if pointer.number() == number: 
            self.head = pointer.next # in case first item in list is thing that needs to be removed
            return
        while pointer != None:
            if pointer.number() == number:
                pointer_2.next = pointer.next
                return
            pointer_2 = pointer
            pointer = pointer.next

    def remove_all(self, number):
        '''removes ALL occurrences of the specified Course'''
        pointer = self.head
        pointer_2 = None
        while pointer.number() == number: 
            self.head = pointer.next # in case multiple items at first in list are things that needs to be removed
            pointer = pointer.next
        while pointer != None:
            if pointer.number() == number:
                while pointer.number() == number: #in case there are multiple of same course num in a row
                    pointer = pointer.next
                pointer_2.next = pointer
            pointer_2 = pointer
            pointer = pointer.next

    def find(self, number):
        '''find the first occurrance of the specified course in the list or return -1'''
        pointer = self.head
        while pointer != None:
            if pointer.number() == number:
                return pointer
            pointer = pointer.next
        return -1

    def size(self):
        '''return the number of items in the list'''
        pointer = self.head
        counter = 0
        while pointer != None:
            counter += 1
            pointer = pointer.next
        return counter

    def calculate_gpa(self):
        '''return the GPA using all courses in the list'''
        pointer = self.head
        total_cdt_hrs = 0.0
        points = 0.0
        while pointer != None:
            points += pointer.grade() * pointer.credit_hr()
            total_cdt_hrs += pointer.credit_hr()
            pointer = pointer.next
        if total_cdt_hrs == 0:
            total_cdt_hrs += 1 #this is so there is no division by zero error
        return points / total_cdt_hrs

    def is_sorted(self):
        '''return True if the list is sorted by Course Number, False otherwise'''
        try:
            pointer = self.head.next
            pointer_2 = self.head
            while pointer != None:
                if pointer.number() < pointer_2.number():
                    return False
                pointer_2 = pointer
                pointer = pointer.next
            return True
        except: #in case the list is empty; pointer cannot == self.head.next
            return True
            
    def __str__(self):
        '''returns a string with each Course’s data on a separate line'''
        return_str = []
        pointer = self.head
        while pointer != None:
            return_str.append(pointer.__str__())
            pointer = pointer.next
        return "\n".join(return_str) # I wasn't sure how else to print the list to the console

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.head != None:
            save_point = self.head
            self.head = self.head.next
            return save_point
        else:
            raise StopIteration

    
        


