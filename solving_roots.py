# solving_roots.py 

# =======================================
# ============ notes 'solving quadratic equations'======================
# solving_quadratics.py 
# https://www.cliffsnotes.com/study-guides/algebra/algebra-i/quadratic-equations/solving-quadratic-equations#:~:text=There%20are%20three%20basic%20methods,formula%2C%20and%20completing%20the%20square.

# =======================================

# packages:
import math 
import numpy as np 

# ============ solving_roots.py ======================
class SolvingQuadratics:
    def __init__(self, a, b, c):

        # ------ instance variables ---------
        self.a    = a
        self.b    = b
        self.c    = c
  
    def solving_using_quadratic(self):
        print('=========== start quadratic method ===========')
        D = self.b**2 -4*self.a*self.c
        print('\nD: ',D)
        if (D == 0):
            root1 = -self.b / (2*self.a)
            root2 = None
            print('\n ',self.a,self.b,self.c)
            print('root1: ',root1)
        elif (D > 0):
            root1 = (-self.b + math.sqrt(D)) / (2*self.a)
            root2 = (-self.b - math.sqrt(D)) / (2*self.a)
            print('\n ',self.a,self.b,self.c)
            print('root1: ',root1)
            print('root2: ',root2)
        else:
            root1 = None
            root2 = None
            print('root1: ',root1)
            print('root2: ',root2)

        roots = [root1,root2]
        print('=========== end quadratic method ===========')

        return roots       
    
    def solving_using_factoring(self):
        print('=========== start factor method ===========')
        print('\nr1*r2 = a * c')
        print('r1+r2 = b\n')

        print('\npre',self.a,self.b,self.c)

        if ((self.b%self.a) == 0) and ((self.c%self.a) == 0):
            self.b = self.b/self.a
            self.c = self.c/self.a
            self.a = 1

        W = int(self.a * self.c)
        #print('\nW',W)
        print('post',self.a,self.b,self.c)
        
        factors_ = np.array([])
        for w in range(1,abs(W)+1):
            if (W%w == 0):
                factors_ = np.append(factors_, w) 
                #print('w',w)

        print('W', W)
        print('factors_', factors_)
        

        # r1*r2 == a*C
        rs = np.array([])
        if (len(factors_) == 0 ):

            for i in factors_:
                for j in factors_:
                    if (i *j == W) and (i +j == self.b):
                        rs = np.append(rs, i)
                        rs = np.append(rs, j)
                    elif (-i *j == W) and (-i +j == self.b):
                        rs = np.append(rs, -i)
                        rs = np.append(rs, j)
                    elif (i * -j == W) and (i -j == self.b):
                        rs = np.append(rs, i)
                        rs = np.append(rs, -j)
                    elif (-i * -j == W) and (-i -j == self.b):
                        rs = np.append(rs, -i)
                        rs = np.append(rs, -j)
                    else:
                        pass
        else: 
            print("there is no integer factors/roots in this quadratic")

        rs = np.unique(rs)
        print('rs',rs)

        if (len(rs) >= 2 ):
            print('\n(x + ',rs[0],')','(x + ',rs[1],')\n')
        elif (len(rs) >= 1 ):
            print('\n(x + ',rs[0],')\n')
        else: 
            pass 

        roots = np.array([])
        if (len(rs) > 0 ):
            for r in rs:
                roots = np.append(roots, -r)
            print('\nroots', roots, '\n')
        print('=========== end factor method ===========')

        return roots   

