from parse_polynomial import parse_polynomial

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
        return polynomialString

#
# textPolynomial1 = "5"
#
# poly1 = Polynomial(parse_polynomial(textPolynomial1))
# print(poly1.print())