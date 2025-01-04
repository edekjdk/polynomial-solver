from parse_polynomial import parse_polynomial
import numpy as np
import matplotlib.pyplot as plt

class Polynomial:
    def __init__(self, poly: list[dict[int, int]]) -> None:
        self.poly = poly
    def print(self) -> str:
        superscript_dict = {
            '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
            '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
        }

        polynomialString = ''
        for power, coeff in self.poly:
            if power == 0:  # Wyraz wolny, bez zmiennej
                term = f"{coeff}"
            elif power == 1:  # x zamiast x¹
                term = f"{coeff}x"
            else:
                term = f"{coeff}x{''.join(superscript_dict[digit] for digit in str(power))}"

            if coeff == 1 and power > 0:
                term = term.replace("1x", "x")
            elif coeff == -1 and power > 0:
                term = term.replace("-1x", "-x")

            # Dodawanie znaku "+" dla dodatnich współczynników (poza pierwszym składnikiem)
            if coeff > 0 and polynomialString:
                polynomialString += f"+{term}"
            else:
                polynomialString += term
        #print(polynomialString)
        return polynomialString

    def degree(self) -> int:
        #first, not the best approach

        # degree = 0
        # for part in self.poly:
        #     if part[0] > degree:
        #         degree = part[0]
        # print(degree)

        #second, the easiest way
        #print(len(self.poly))

        #third, not the best but the most "python way"
        #print(max(i[0] for i in self.poly))
        return max(i[0] for i in self.poly)


    def solve(self, real_only:bool = False) -> list[int]:
        degree = max(i[0] for i in self.poly)
        tab = [0 for i in range(degree + 1)]
        for i in self.poly:
            tab[degree - i[0]] = i[1]
        roots = np.roots(tab).tolist()

        if complex in list(map(lambda x: type(x), roots)):
            roots = [complex(round(root.real,2), round(root.imag,2)) for root in roots]
            roots = [
                root.real if root.imag == 0 else root
                for root in roots
            ]
            if real_only:
                if float in list(map(lambda x: type(x), roots)):
                    roots = [root for root in roots if type(root) == float]

        else:
            roots = sorted(roots, reverse=False)
            roots = [round(i, 2) for i in roots]

            #sorted_roots = list(map(lambda x:round(x, 3), sorted_roots)) // second way to do this

        return roots


    def chart(self) -> None:
        degree = max(i[0] for i in self.poly)
        tab = [0 for i in range(degree + 1)]

        for i in self.poly:
            tab[degree - i[0]] = i[1]
        #roots = [round(i,2 ) for i in np.roots(tab).tolist()]

        # Tworzenie wykresu na podstawie tablicy współczynników
        x = np.linspace(-10, 10, 1000)  # Generowanie wartości x w zakresie [-10, 10]
        y = np.polyval(tab, x)  # Obliczenie wartości wielomianu dla każdego x

        # Rysowanie wykresu
        plt.ylim(-10, 10)
        plt.xlim(-10, 10)
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Oś X
        plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
        plt.plot(x, y, label="polynomial chart", color="blue")
        # for i in np.roots(tab).tolist():
        #     plt.plot(i,0, marker='o', label=i)
        #plt.scatter(roots, np.zeros_like(roots), color="black", label = roots)
  # Oś Y
        plt.title("polynomial chart")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        plt.show()


w1 = "x^3+x^2-4x-7"

w1 = Polynomial(parse_polynomial(w1))

# print(w1.print())
# print(w1.degree())
print(w1.solve(real_only=True))
w1.chart()
# w1.print()

