import numpy as np
import matplotlib.pyplot as plt

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

        for w in args:
            tab = [0 for i in range(w.degree() + 1)]

            for i in w.poly:
                tab[w.degree() - i[0]] = i[1]
            y = np.polyval(tab, x)
            plt.plot(x, y, label=w.print())
        plt.legend()
        plt.show()
