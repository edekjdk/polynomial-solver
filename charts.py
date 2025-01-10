import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations

class Charts:
    @staticmethod
    def draw_chart(*args, x_range=[-10,10], y_range=[-10,10], common_points=False):

        x = np.linspace(-10, 10, 1000)


        plt.ylim(y_range[0], y_range[1])
        plt.xlim(x_range[0], x_range[1])
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--") 
        plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
        # for i in np.roots(tab).tolist():
        #     plt.plot(i,0, marker='o', label=i)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        Charts._draw_multiple_charts(x,*args)
        if common_points:
            Charts._draw_common_points(*args)
        plt.legend()
        plt.show()

    @staticmethod
    def _draw_multiple_charts(x,*args):
        for w in args:
            y = np.polyval(w.table_of_coefficients, x)
            plt.plot(x, y, label=w.print())

    @staticmethod
    def _draw_common_points(*args):
        all_common_points = []
        for w1, w2 in combinations(args, 2):
            w = (w1-w2)
            x = np.roots(w.table_of_coefficients).tolist()
            y = np.polyval(w1.table_of_coefficients, x).tolist()
            for x1,y2 in zip(x,y):
                if type(x1) == complex:
                    if x1.imag == 0:
                        all_common_points.append([x1.real, y2.real])
                else:
                    all_common_points.append([x1,y2])
        for i in all_common_points:
            plt.scatter(*i, color="black", zorder=10)





