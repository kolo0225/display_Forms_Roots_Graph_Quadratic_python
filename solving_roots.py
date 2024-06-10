# solving_roots.py 

# ============ 'solving quadratic equations'======================

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
  
    # solving quaderatic equation using quadratic formula
    def solving_using_quadratic(self):
        print('=========== start quadratic method ===========')
        
        # discriminant
        D = self.b**2 -4*self.a*self.c
        print(f'\nD: {D}, where D is the discriminant')
        
        # for D==0 there is one root
        if (D == 0):
            root1 = -self.b / (2*self.a)
            root2 = None
            
            # print (a,b,c & root1)
            print(f'\nfor:\na = {self.a}, b = {self.b}, c = {self.c}')
            print('root1: ',root1)
            
        # For positive D (2 roots) 
        elif (D > 0):
            root1 = (-self.b + math.sqrt(D)) / (2*self.a)
            root2 = (-self.b - math.sqrt(D)) / (2*self.a)
            
            # print (a,b,c, root1, root2)
            print(f'\nfor:\na = {self.a}, b = {self.b}, c = {self.c}')
            print('root1: ',root1)
            print('root2: ',root2)
            
        # For negative D (2 roots) -> there is no solution (sqrt >= 0)
        else:
            
            root1 = None
            root2 = None
            
            # print (a,b,c, root1, root2)
            print(f'\nfor:\na = {self.a}, b = {self.b}, c = {self.c}')
            print('root1: ',root1)
            print('root2: ',root2)

        # roots is a list that holds root1 & root2
        roots = [root1,root2]
        print('=========== end quadratic method ===========')

        return roots       
    
    # solving quadratic equation using factoring
    def solving_using_factoring(self):
    
        # print commands 
        print('=========== start factor method ===========')
        print('\nr1*r2 = a * c')
        print('r1+r2 = b\n')

        print(f'\nbefore simplification: a = {self.a}, b = {self.b}, c = {self.c}')

        # if no remainder -> simplification
        if ((self.b%self.a) == 0) and ((self.c%self.a) == 0):
            self.b = self.b/self.a
            self.c = self.c/self.a
            self.a = 1

        W = int(self.a * self.c)
        
        print(f'\nafter simplification: a = {self.a}, b = {self.b}, c = {self.c}')
        
        factors_ = np.array([])
        for w in range(1,abs(W)+1):                # '+1' since range starts at '1' 
            if (W%w == 0):
                factors_ = np.append(factors_, w) 
        
        # prints
        print(f'\na*c = {W}')
        print(f'factors list = {factors_}')
        

        # r1*r2 == a*C
        rs = np.array([])
        if (len(factors_) != 0 ):

            for i in factors_:
                for j in factors_:
                    # finds positive & negative factors 
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
            print('there is no integer factors/roots that satisfy this quadratic equation')

        # removes repeat values
        rs = np.unique(rs)
        if len(rs) > 0: 
            print(f'\nfactor list that satisfy this equation: ,{rs}')
        else:
            print('there is no integer factors/roots that satisfy this quadratic equation')
            
        # formula (x + root1 )(x + root2)
        if (len(rs) >= 2 ):
            print(f'\n(x + {rs[0]})*(x + {rs[1]})\n')
        elif (len(rs) >= 1 ):
            print(f'\n(x + {rs[0]})')
        else: 
            pass

        # soling for x in (x + root1 )(x + root2) ==> x = - root1, x = - root2
        roots = np.array([])
        if (len(rs) > 0 ):
            for r in rs:
                roots = np.append(roots, -r)
            print(f'\nroots: {roots}')
        else:
            pass
        
        print('\n=========== end factor method ===========')
        return roots   

