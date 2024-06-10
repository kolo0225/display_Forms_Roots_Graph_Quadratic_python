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

    # produces multi-line plot
    def multiple_line_plots(self):

        # x limits
        x_min_lim = min(self.x) -1
        x_max_lim = max(self.x) +1

        # root_list (just the x-axis -> shows where the graph is at y=0 (roots)
        roots = np.array([])
        for x_ in self.x:
            roots = np.append(roots, 0)

        # sets x limits
        plt.xlim((x_min_lim,x_max_lim))   
        
        # plot line
        plt.plot(self.x, self.y, color='r',)
        plt.plot(self.x, roots, color='b')

        plt.show()

# ====================================================================
