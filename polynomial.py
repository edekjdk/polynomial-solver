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

        test = [i for i in self.poly if i[1] != 0]
        polynomialString = ''
        for power, coeff in test:
            if power == 0:
                term = f"{coeff}"
            elif power == 1:  # x zamiast x¹
                term = f"{coeff}x"
            else:
                term = f"{coeff}x{''.join(superscript_dict[digit] for digit in str(power))}"

            if coeff == 1 and power > 0:
                term = term.replace("1x", "x")
            elif coeff == -1 and power > 0:
                term = term.replace("-1x", "-x")

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


    def chart(self, x_range:list[int]=[-10,10], y_range:list[int]=[-10,10]) -> None:
        #degree = max(i[0] for i in self.poly)
        degree = self.degree()
        tab = [0 for i in range(degree + 1)]

        for i in self.poly:
            tab[degree - i[0]] = i[1]
        #roots = [round(i,2 ) for i in np.roots(tab).tolist()]
        roots = np.roots(tab).tolist()
        notComplex = [round(i.real, 2) for i in roots if i.imag == 0.0]
        # for i in roots:
        #     if type(i) == complex:
        #         roots.remove(i)

        x = np.linspace(-10, 10, 1000)
        y = np.polyval(tab, x)

        plt.ylim(y_range[0], y_range[1])
        plt.xlim(x_range[0], x_range[1])
        plt.axhline(0, color="black", linewidth=0.8, linestyle="--")  # Oś X
        plt.axvline(0, color="black", linewidth=0.8, linestyle="--")
        plt.plot(x, y, label="polynomial chart", color="blue")
        # for i in np.roots(tab).tolist():
        #     plt.plot(i,0, marker='o', label=i)
        plt.scatter(notComplex, np.zeros_like(notComplex), color="black", label=notComplex)
        plt.title("polynomial chart")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.grid(True)
        plt.legend()
        plt.show()

    def addPolynomials(self, *args):
        result = {}
        for power, coeff in self.poly:
            if power in result:
                result[power] += coeff
            else:
                result[power] = coeff
        for polynomial in args:
            for power, coeff in polynomial.poly:
                if power in result:
                    result[power] += coeff
                else:
                    result[power] = coeff
        sorted_result = sorted(result.items(), key=lambda x: x[0], reverse=True)
        return Polynomial(sorted_result)

    def __add__(self, *args):
        return self.addPolynomials(*args)

    def substractPolynomials(self, *args):
        result = {}
        for power, coeff in self.poly:
            if power in result:
                result[power] -= coeff
            else:
                result[power] = coeff
        for polynomial in args:
            for power, coeff in polynomial.poly:
                if power in result:
                    result[power] -= coeff
                else:
                    result[power] = coeff
        sorted_result = sorted(result.items(), key=lambda x: x[0], reverse=True)
        return Polynomial(sorted_result)

    def __sub__(self, *args):
        return self.substractPolynomials(*args)

w1 = "3x^3-x^2-4x-7"
w2 = "x+3"
w3 = "x+3-5"

w1 = Polynomial(parse_polynomial(w1))
w2 = Polynomial(parse_polynomial(w2))
w3 = Polynomial(parse_polynomial(w3))

w4 = w1.addPolynomials(w2,w3)
w5 = w1 + w3

w6 = w2.substractPolynomials(w3)

w7 = w1-w2

print(w7.print())



#print(w1.print())
# print(w1.degree())
#print(w1.solve(real_only=True))
#print(w1.solve())
w1.chart(y_range=[-20,20])
# w1.print()

