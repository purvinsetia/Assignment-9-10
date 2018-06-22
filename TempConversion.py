class Temperature:
            
    def convtoF(self,cel_temp):
        self.ctemp = cel_temp
        Ftemp = (self.ctemp*1.8) + 32
        print("Temperature in Farenheit is-> ",Ftemp)
    def convtoC(self,fah_temp):
        self.ftemp = fah_temp
        Ctemp = (self.ftemp-32)/1.8
        print("Temperature in Celcius is-> ",Ctemp)

check = int(input("Enter Input(1/2) :\n1.Farenheit to Celsius\n2.Celsius to Farenheit\n"))
con = Temperature()

if (check==1):
    t=float(input("Enter Temperature in Farenheit-> "))
    con.convtoC(t)
elif(check==2):
    t=float(input("Enter Temperature in Celcius-> "))
    con.convtoF(t)
else:
    print("Wrong Input")
    
