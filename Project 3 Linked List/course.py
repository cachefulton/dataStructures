'''
This file will receive data from main file and return the information accordingly.
'''
class Course:
    def __init__(self, number=0, name="", credit_hr=0.0, grade=0.0):
        self.num = number
        self.na = name
        self.credit = credit_hr
        self.gra = grade
        self.next = None
        #I put these next calls in here because the pytest won't work for one section if I don't
        self.number()
        self.credit_hr()
        self.name()
        self.grade()

    def number(self):
        '''retrieve Course Number as an integer'''
        if float(self.num) < 0.0:
            raise ValueError
        else:
            return int(self.num)

    def name(self):
        '''retrieve Course Name as a string'''
        if self.na == None:
            raise ValueError
        else:
            return str(self.na)

    def credit_hr(self):
        '''retrieve Credits as a floating-point number'''
        if float(self.credit) < 0.0:
            raise ValueError
        else:
            return float(self.credit)

    def grade(self):
        '''retrieve Grade as a numeric value in range 4.0 – 0.0'''
        self.gra = float(self.gra)
        if self.gra >= 0.0 and self.gra <= 4.0:
            return self.gra
        else:
            raise ValueError

    def __str__(self):
        return f"cs{self.number()} {self.name()}, Grade: {self.grade()} Credit Hours: {self.credit_hr()}"

