polynomial = "2x^2-4x^2+x+x"
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
            pows.append(i.split("^")[1])
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

    for pow,new_digit in zip(pows, new_digits):
        if pow not in result:
            result[pow] = int(new_digit[0:-1])
        else:
            result[pow] += int(new_digit[0:-1])


    wynik = [str(s)+"x" for s in list(result.values())]

    return list(result.keys()), wynik

pows, digits = splitPolynomial(polynomial)

def printPolynomial(pows, digits):
    superscript_dict = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
    }

    lastresult = ''

    for i in range(len(pows)):
        item = "{}{}".format(digits[i], ''.join(superscript_dict[digit] for digit in str(pows[i])))
        if item[0]!="-" and i != 0:
            lastresult += "+{}".format(item)
        else:
            lastresult += item
    lastresult = lastresult.replace("1x", "x")
    lastresult = lastresult.replace("x¹", "x")
    return lastresult


print(printPolynomial(pows, digits))







#refactor
#add comments
#build one function of that functionality
