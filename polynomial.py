from parse_polynomial import parse_polynomial
import numpy as np
import matplotlib.pyplot as plt

class Polynomial:
    def __init__(self, poly):
        self.poly = poly

    def print(self):
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
        print(polynomialString)

    def degree(self):
        degree = 0
        for part in self.poly:
            if part[0] > degree:
                degree = part[0]
        print(degree)

    def solve(self):
        degree = 0
        for part in self.poly:
            if part[0] > degree:
                degree = part[0]

        tab = [0 for i in range(degree + 1)]

        for i in self.poly:
            tab[degree - i[0]] = i[1]

        print(tab)
        roots = np.roots(tab)
        sorted_roots = sorted(roots, key=lambda x: x.real)
        print(sorted_roots)

    def chart(self):
        degree = 0
        for part in self.poly:
            if part[0] > degree:
                degree = part[0]

        tab = [0 for i in range(degree + 1)]

        for i in self.poly:
            tab[degree - i[0]] = i[1]



        # Tworzenie wykresu na podstawie tablicy współczynników
        x = np.linspace(-5.5, 5.5, 1000)  # Generowanie wartości x w zakresie [-10, 10]
        y = np.polyval(tab, x)  # Obliczenie wartości wielomianu dla każdego x

        # Rysowanie wykresu
        plt.figure(figsize=(8, 6))
        plt.ylim(-15, 15)
        plt.xlim(-15, 15)

        plt.plot(x, y, label="polynomial chart", color="blue")
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Oś X
        plt.axvline(0, color="black", linewidth=0.8, linestyle="--")  # Oś Y
        plt.title("polynomial chart")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        plt.show()


w1 = "x^3-2x-x+1"

w1 = Polynomial(parse_polynomial(w1))

w1.print()
w1.degree()
w1.solve()
w1.chart()
w1.print()