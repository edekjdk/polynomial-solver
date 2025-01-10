import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations





class Charts:
    @staticmethod
    def draw_chart(*args, x_range=[-10,10], y_range=[-10,10]):

        x = np.linspace(-10, 10, 1000)


        plt.ylim(y_range[0], y_range[1])
        plt.xlim(x_range[0], x_range[1])
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Oś X
        plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
        # for i in np.roots(tab).tolist():
        #     plt.plot(i,0, marker='o', label=i)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        Charts._draw_multiple_charts(x,*args)
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
        all = []
        for w1, w2 in combinations(args, 2):
            w = (w1-w2)
            tab = [0 for i in range(w.degree() + 1)]

            for i in w.poly:
                tab[w.degree() - i[0]] = i[1]
            x = np.roots(tab).tolist()

            tabw1 = [0 for i in range(w1.degree() + 1)]

            for i in w1.poly:
                tabw1[w1.degree() - i[0]] = i[1]

            y = np.polyval(tabw1, x).tolist()
            for x1,y2 in zip(x,y):
                if type(x1) == complex:
                    if x1.imag == 0:
                        all.append([x1.real, y2.real])
                else:
                    all.append([x1,y2])
        for i in all:
            plt.scatter(*i, color="black", zorder=10)





