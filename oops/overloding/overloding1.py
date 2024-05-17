class Area:
    
    def findArea(self,x):
        print("Area of square: ",x*x)
    
    def findArea(self,x,y):
        print("Area of rectangle: ",x*y)
    
    
    def findArea(self,x,y,z):
        s=(x+y+z)/2
        area=(s*(s-x)*(s-y)*(s-z))**0.5
        print("Area of triangle: ",area)
        

a  = Area()
a.findArea(10)
# a.findArea(10,20)
# a.findArea(10,20,30)        
        
        
            