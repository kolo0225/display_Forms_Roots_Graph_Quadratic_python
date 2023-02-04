# graphing_quadratic.py 

# packages:
import numpy as np 
import matplotlib.pyplot as plt

# ============ solving_roots.py ======================
class Display:

    def __init__(self, x, y):

        # ------ instance variables ---------
        self.x     = x
        self.y     = y

    def multiple_line_plots(self):

        x_min_lim = min(self.x) -1
        x_max_lim = max(self.x) +1

        roots = np.array([])
        for x_ in self.x:
            roots = np.append(roots, 0)

        plt.xlim((x_min_lim,x_max_lim))   
        
        # plot line
        plt.plot(self.x, self.y, color='r',)
        plt.plot(self.x, roots, color='b')

        plt.show()

# ====================================================================
