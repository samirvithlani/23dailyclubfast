from multipledispatch import dispatch
class Shape:
    
    @dispatch(int)
    def findArea(self,x):
        print("Area of square: ",x*x)
    
    @dispatch(int,int)
    def findArea(self,x,y):
        print("Area of rectangle: ",x*y)    
    
    @dispatch(int,int,int)
    def findArea(self,x,y,z):
        print("Area of triangle: ",x*y*z)
        
    @dispatch(float)    
    def findArea(self,a):
        print("Area of circle: ",3.14*a*a)    


s = Shape()
#s.findArea(10,20,30)        
s.findArea(12.22)
        
            
'''
search(string pname)
search(string pname, string pcolor)
search(string pname,int var)
search(string pname, int var,int cap)

'''            
        
        