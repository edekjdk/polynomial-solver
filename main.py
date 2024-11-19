polynomial = "5x^22-6x^33-2x^2-x^4-x^2"
# polynomial = input("Enter a polynomial: ")

def splitPolynomial(polynomial):
    powers = []
    pows = []
    digits = []
    start = 0
    for i in range(len(polynomial)):
        if polynomial[i] == "-" or polynomial[i] == "+":
            powers.append(polynomial[start:i])
            start = i
        if i == len(polynomial) - 1:
            powers.append(polynomial[start:i+1])
    for i in powers:
        digits.append(i.split("^")[0])
        if len(i.split("^")) == 2:
            pows.append(i.split("^")[1])
        else:
            pows.append(1)
    return pows, digits

def printPolynomial(pows, digits):
    superscript_dict = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
    }

    lastresult = ''

    for i in range(len(pows)):
        lastresult = lastresult + "{}{}".format(digits[i], ''.join(superscript_dict[digit] for digit in str(pows[i])))
    return lastresult

print(printPolynomial(splitPolynomial(polynomial)[0],splitPolynomial(polynomial)[1]))

#refactor
#add comments
#build one function of that functionality
