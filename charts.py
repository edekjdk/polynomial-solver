import numpy as np
import matplotlib.pyplot as plt

class Charts:
    @staticmethod
    def draw_chart(*args):

        x = np.linspace(-10, 10, 1000)


        plt.ylim(-10, 10)
        plt.xlim(-10, 10)
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
            plt.plot(x, y, label="polynomial chart")

        plt.show()
