class Circle:
    pi = 3.14

    def __init__(self,rad):
        self.r=rad

    def getArea(self):
        area = Circle.pi * self.r * self.r
        print ("area of the circle is-> %d"%(area))
    def getCircumference(self):
        cir = 2 * Circle.pi * self.r
        print ("Circumference of the circle is-> %d"%(cir))

radius = int(input("enter radius of the circle-> "))

c1= Circle(radius)
c1.getCircumference()
c1.getArea()
