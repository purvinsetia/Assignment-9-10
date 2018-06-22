class Expenditure:
    def __init__(self,ex,sav):
        self.expend=ex
        self.savings=sav
    def display(self):
        print("Expenditure= %d\nSavings= %d"%(self.expend,self.savings))
    def calculateSalary(self):
        self.sal=self.expend+self.savings
    def dispSal(self):
        print("Total Salary= %d"%(self.sal))

exp=Expenditure(1000,15000)
exp.display()
exp.calculateSalary()
exp.dispSal()

    
        
