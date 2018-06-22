class Student:

    def __init__(self,na,rn):
        self.name=na
        self.rollno=rn
    def disp(self):
        print ("Name-> %s\nRoll No-> %d"%(self.name,self.rollno))

name = input("Enter your name-> ")
rollno = int(input("Enter your roll no.-> "))

s1=Student(name,rollno)
s1.disp()
    
        
        
