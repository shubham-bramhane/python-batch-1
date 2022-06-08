# single inheritance 


class Person():
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print('full name:----',self.firstname,self.lastname)

class Student(Person):
    def __init__(self, fname, lname,roll_no):
        super().__init__(fname, lname)
        self.rollno=roll_no

    def studentdata(self):
        print('student information---->')
        print('student firstname---->',self.firstname)
        print('student lastname---->',self.lastname)
        print('student roll no---->',self.rollno)





x=Student("shubham",'bramhane',21)
# x.studentdata()
x.printname()