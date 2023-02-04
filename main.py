# main.py
# NOTES:
#    ISSUES WITH:
#        1.
#        line 91, in solving_using_factoring
#        print('\n(x + ',rs[0],')','(x + ',rs[1],')\n')
#        IndexError: index 0 is out of bounds for axis 0 with size 0

# =======================================
# Importing  files.py 
from  change_forms import FormChanger
from solving_roots import SolvingQuadratics
from graphing_quadratic import  Display

# packages:
import numpy as np 

# ============ control center ============

a = 'vertix_to_standard'
b = 'standard_to_vertix'
c = 'using_quadratic'
d = 'using_roots_r1r2'
e = 'standard_r1r2_graph'
f = 'standard_quadratic_graph'
g = 'vertix_quadratic_graph'
n = e 
# ============ Variables ==================
a = 4
b = -8
c = 5
h = 1
k = 1
x =  np.arange(-5,5,1)
# ==========================================

# Python Switch Case Statement using Class
class StepModuleExecSwitch:

    def switch(self, n):
        default = "too many entries"

        #getattr(obj, key, def)
        return getattr(self, n, lambda: default)()

    def standard_to_vertix(self):

        y = np.array([])
        for x_ in x: 
            Vertex_obj =  FormChanger(a, b, c, h, k, x_)
            y= np.append(y,Vertex_obj.from_standard_to_vertex())
        print('this is a x array: ',x)
        print('this is a y array: ',y)

        return

    def vertix_to_standard(self):

        y = np.array([])
        for x_ in x: 
            Standard_obj =  FormChanger(a, b, c, h, k, x_)
            y= np.append(y,Standard_obj.from_vertex_to_standard())
        print('this is a x array: ',x)
        print('this is a y array: ',y)

        return

    def using_quadratic(self):

        Quadratic_obj =  SolvingQuadratics(a, b, c)
        Quadratic_obj.solving_using_quadratic()

        return

    def using_roots_r1r2(self):

        Factored_obj =  SolvingQuadratics(a, b, c)
        Factored_obj.solving_using_factoring()

        return
    
    def standard_r1r2_graph(self):

        y = np.array([])
        for x_ in x: 
            Standard_obj =  FormChanger(a, b, c, h, k, x_)
            y= np.append(y,Standard_obj.from_vertex_to_standard())
        print('this is a x array: ',x)
        print('this is a y array: ',y)

        Factored_obj =  SolvingQuadratics(a, b, c)
        Factored_obj.solving_using_factoring()

        Display_obj =  Display(x, y)
        Display_obj.multiple_line_plots()

        return

    def standard_quadratic_graph(self):

        y = np.array([])
        for x_ in x: 
            Standard_obj =  FormChanger(a, b, c, h, k, x_)
            y= np.append(y,Standard_obj.from_vertex_to_standard())
        print('this is a x array: ',x)
        print('this is a y array: ',y)

        Quadratic_obj =  SolvingQuadratics(a, b, c)
        roots = Quadratic_obj.solving_using_quadratic()

        Display_obj =  Display(x, y)
        Display_obj.multiple_line_plots()

        return

    def vertix_quadratic_graph(self):

        y = np.array([])
        for x_ in x: 
            Vertex_obj =  FormChanger(a, b, c, h, k, x_)
            y= np.append(y,Vertex_obj.from_standard_to_vertex())
        print('this is a x array: ',x)
        print('this is a y array: ',y)

        Quadratic_obj =  SolvingQuadratics(a, b, c)
        roots = Quadratic_obj.solving_using_quadratic()

        Display_obj =  Display(x, y)
        Display_obj.multiple_line_plots()

        return

obj = StepModuleExecSwitch()
obj.switch(n)

