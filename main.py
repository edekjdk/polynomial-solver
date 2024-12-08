from operator import index

import numpy as np

polynomial = "1x^2-2x+1"
# polynomial = input("Enter a polynomial: ")

def splitPolynomial(polynomial):
    powers = []
    pows = []
    digits = []
    start = 0
    for i in range(len(polynomial)):
        if i!=0 and polynomial[i] == "-" or polynomial[i] == "+":
            powers.append(polynomial[start:i])
            start = i
        if i == len(polynomial) - 1:
            powers.append(polynomial[start:i+1])
    for i in powers:
        digits.append(i.split("^")[0])
        if len(i.split("^")) == 2:
            pows.append(int(i.split("^")[1]))
        elif "x" not in i:
            pows.append('0')
        else:
            pows.append('1')

    new_digits = []
    for i in digits:
        if i == "-x":
            new_digits.append("-1x")
        if i == "+x":
            new_digits.append("+1x")
        if i != "+x" and i != "-x":
            new_digits.append(i)

    result = {}

    for pow,new_digit in zip(pows, new_digits):
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


    wynik = [str(s)+"x" for s in list(result.values())]
    return list(result.keys()), wynik

pows, digits = splitPolynomial(polynomial)

def printPolynomial(pows, digits):
    zipped = zip(pows, digits)

    sorted_zipped = sorted(zipped, key=lambda x: int(x[0]), reverse=True)
    sorted_keys, sorted_values = zip(*sorted_zipped)

    pows= list(sorted_keys)
    digits = list(sorted_values)

    superscript_dict = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
    }

    lastresult = ''

    for i in range(len(pows)):
        item = "{}{}".format(digits[i], ''.join(superscript_dict[digit] for digit in str(pows[i])))
        if item[item.index('x'):] == "x¹":
            item = item[:item.index('x')+1]
        if item[0]!="-" and i != 0:
            lastresult += "+{}".format(item)
        else:
            lastresult += item

    lastresult = lastresult.replace("1x", "x")
    lastresult = lastresult.replace("x⁰", "")

    return lastresult, pows, digits


resultToPrint, pows, digits = printPolynomial(pows, digits)

print(resultToPrint)



def solvePoly(pows, digits):
    pows = [int(i) for i in pows]
    pom = []
    coeffs = [i for i in range(pows[0],pows[-1]-1,-1)]
    for i in coeffs:
        if i in pows:
            pom.append(int(digits[pows.index(i)][:digits[pows.index(i)].index('x')]))
        else:
            pom.append(0)
    print(np.roots(pom))

solvePoly(pows, digits)

#refactor
#add comments
#build one function of that functionality
