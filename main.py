# main.py


# =======================================
# Importing  files.py 
from  change_forms import FormChanger
from solving_roots import SolvingQuadratics
from graphing_quadratic import  Display

# packages:
import numpy as np 

# ============ control center ============

a = 'standard_to_vertix_roots_n_graph' # from standard form to vertix - prints the exact roots and a graph
b = 'vertix_to_standard_n_graph'       # from vertix form to standard - prints a graph
c = 'roots_using_quadratic'            # prints the exact roots of the quadratic equation starting from standard form, using quadratic formula
d = 'roots_using_factoring'            # prints the whole roots of the quadratic equation if any starting from standard form, using factoring

n = d
# ============ Variables ==================
a = 1
b = 4
c = -12
h = 3
k = -1
x =  np.arange(-5,6,1)  # x is a range of values  => y = a range of values 
# ==========================================

# Python Switch Case Statement using Class
class StepModuleExecSwitch:

    def switch(self, n):
        default = "too many entries"

        #getattr(obj, key, def)
        return getattr(self, n, lambda: default)()

    #  vertx form  y = a*(x - h)**2 + k =>  standard form y= a*x**2 + b*x + c 
    def standard_to_vertix_roots_n_graph(self):

        y = np.array([])
        for x_ in x: 
            # solving quadratic  standard form y= a*x**2 + b*x + c =>  vertx form  y = a*(x - h)**2 + k 
            # values a, b, c, x are used
            Vertex_obj =  FormChanger(a, b, c, h, k, x_)
            y = np.append(y,Vertex_obj.from_standard_to_vertex())
            
        print(f'\nthis is a x array: {x}')
        print(f'this is a y array: {y}\n')
        
        # find roots  using quadratic formula
        Quadratic_obj =  SolvingQuadratics(a, b, c)
        Quadratic_obj.solving_using_quadratic()
        
        # plots the the quadratic
        Display_obj =  Display(x, y)
        Display_obj.multiple_line_plots()

        return

    #  standard form y= a*x**2 + b*x + c  => vertx form  y = a*(x - h)**2 + k 
    def vertix_to_standard_n_graph(self):

        y = np.array([])
        for x_ in x: 
            # solving quadratic  vertx form  y = a*(x - h)**2 + k =>  standard form y= a*x**2 + b*x + c 
            # values a, x, h, k are used
            Standard_obj =  FormChanger(a, b, c, h, k, x_)
            y= np.append(y,Standard_obj.from_vertex_to_standard())
            
        print(f'\nthis is a x array: {x}')
        print(f'this is a y array: {y}\n')
        
        # plots the the quadratic
        Display_obj =  Display(x, y)
        Display_obj.multiple_line_plots()

        return

    def roots_using_quadratic(self):

        # find roots  using quadratic formula
        Quadratic_obj =  SolvingQuadratics(a, b, c)
        Quadratic_obj.solving_using_quadratic()

        return

    def roots_using_factoring(self):

        # find roots using factoring 
        Factored_obj =  SolvingQuadratics(a, b, c)
        Factored_obj.solving_using_factoring()

        return
    

obj = StepModuleExecSwitch()
obj.switch(n)

