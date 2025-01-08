import numpy as np

polynomial = "23x^3-12x^4-2x+2x^2+1"

def splitPolynomial(polynomial):
    powers = []
    pows = []
    digits = []
    start = 0
    for i in range(len(polynomial)):
        if i != 0 and (polynomial[i] == "-" or polynomial[i] == "+"):
            powers.append(polynomial[start:i])
            start = i
        if i == len(polynomial) - 1:
            powers.append(polynomial[start:i + 1])
    for i in powers:
        digits.append(i.split("^")[0])
        if len(i.split("^")) == 2:
            pows.append(int(i.split("^")[1]))
        elif "x" not in i:
            pows.append(0)  # Wyraz wolny
        else:
            pows.append(1)

    new_digits = []
    for i in digits:
        if i == "-x":
            new_digits.append("-1x")
        if i == "+x":
            new_digits.append("+1x")
        if i != "+x" and i != "-x":
            new_digits.append(i)

    result = {}

    for pow, new_digit in zip(pows, new_digits):
        if pow not in result:
            if "x" not in new_digit:
                result[pow] = int(new_digit)
            else:
                result[pow] = int(new_digit[0:-1])
        else:
            if "x" not in new_digit:
                result[pow] += int(new_digit)
            else:
                result[pow] += int(new_digit[0:-1])

    return result

def printPolynomial(result):
    # Sortowanie potęg malejąco
    sorted_terms = sorted(result.items(), key=lambda x: x[0], reverse=True)

    superscript_dict = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
    }

    polynomial_str = ''
    for power, coeff in sorted_terms:
        if power == 0:  # Wyraz wolny, bez zmiennej
            term = f"{coeff}"
        elif power == 1:  # x zamiast x¹
            term = f"{coeff}x"
        else:
            term = f"{coeff}x{''.join(superscript_dict[digit] for digit in str(power))}"

        # Poprawianie zapisu dla współczynników 1 i -1 przy x
        if coeff == 1 and power > 0:
            term = term.replace("1x", "x")
        elif coeff == -1 and power > 0:
            term = term.replace("-1x", "-x")

        # Dodawanie znaku "+" dla dodatnich współczynników (poza pierwszym składnikiem)
        if coeff > 0 and polynomial_str:
            polynomial_str += f"+{term}"
        else:
            polynomial_str += term

    return polynomial_str

# Test
result = splitPolynomial(polynomial)

# print(result)
# polynomial_str = printPolynomial(result)
# print(polynomial_str)
#
#
# print(int("+1"))

#print([(2,11),(3,10)])
test = [(4, 1), (2, -1), (0, -1)]
dl = 4

tab = [0 for i in range(dl+1)]

print(tab)
for i in test:
    print( dl-i[0], i)
    tab[dl-i[0]] = i[1]


print(tab)


