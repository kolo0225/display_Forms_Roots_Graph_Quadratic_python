# change_forms.py 

# ============ notes 'changing form' ========
# change_forms.py 
# https://www.cuemath.com/algebra/standard-form-to-vertex-form/

# standard form      vertex form
# y=a*x**2+b*x+c -> y= a*(x-h)**2+k


# Standard Form to Vertex Form
# using the complete the square method
# -------------------------------
# y= a*x**2+b*x+c -> y= a*(x-h)**2+k
# ex:
# y = -3*x**2 -6*x -9
# y = -3*(x**2 +2*x +3)         # make sure that the coefficient of x**2 =1
# y = -3*(x**2 +2*x +3)         # b= 2 -> (b/2)**2 = (2/2)**2 = 1 =u
# y = -3*(x**2 +2*x +u -u +3)   # after the x term -u & +u 
# use the id (x+u)**2 = x**2 -2*x +u
# -u +3 -> complute
# distribute a
# =======================================

# packages:
import math 
import numpy as np 

# ============ change_forms.py ======================
class FormChanger:
    def __init__(self, a, b, c, h, k, x):

        # ------ instance variables ---------
        self.a    = a
        self.b    = b
        self.c    = c
        self.h    = h
        self.k    = k
        self.x    = x

    def from_vertex_to_standard(self):
        self.b= (-2*self.a*self.h)
        self.c= (self.a*(self.h**2)+self.k)
        print ('\ny= ', self.a,'x^2 + ', self.b, 'x +', self.c, '\n')
        
        y= self.a*self.x**2 + self.b*self.x + self.c 
        print ('x= ', self.x)
        print ('y= ', y)

        return y       

    def from_standard_to_vertex(self):
        print ('====== start vertex form ============')
        b_ = self.b/self.a 
        c_ = self.c/self.a 
        u = (b_/2)**2 
        self.h = -math.sqrt(u)
        self.k = self.a *(-u + c_)
        print('\ny= a(x-h)^2+k')
        print ('y= ', self.a,'(x - ', self.h, ')^2 +', self.k, '\n')
        y = self.a*(self.x - self.h )**2 + self.k
       
        #print ('h = -b/2a', '  -> h = ',- self.b/(2*self.a))         
        D = self.b**2 -4*self.a*self.c
        #print ('k = ah^2 + bh + c', ' -> k =',self.a*(self.h)**2 + self.b*self.h + self.c)         
        print ('k = -D/4*a', ' -> k =',-D /(4*self.a), '\n')         
        print ('x= ', self.x)
        print ('y= ', y)
        print ('====== end vertex form ============')
        return y       









