from parse_polynomial import parse_polynomial

class Polynomial:
    def __init__(self, poly):
        self.poly = poly

    def print(self):
        print(self.poly)


textPolynomial1 = "-3x^3-4+4x^2+2x+322+x"

poly1 = Polynomial(parse_polynomial(textPolynomial1))
poly1.print()