polynomial = "5x^22-6x^33-2x^2-x-x^2-x^2"
# polynomial = input("Enter a polynomial: ")

def showPolynomial(polynomial):
    powers = []
    start = 0
    for i in range(len(polynomial)):
        if polynomial[i] == "-" or polynomial[i] == "+":
            powers.append(polynomial[start:i])
            start = i
    return powers

results = showPolynomial(polynomial)

pows = []
digits = []
for i in results:
    digits.append(i.split("^")[0])
    if len(i.split("^")) == 2:
        pows.append(i.split("^")[1])
    else:
        pows.append(1)

print(pows)
print(digits)

def toSuper(number):
    superscript_dict = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
    }

    # Tworzymy napis z górnymi indeksami dla każdego znaku w wykładniku
    return ''.join(superscript_dict[digit] for digit in str(number))

lastresult = ''
for i in range(len(results)):
    lastresult = lastresult + "{}{}".format(digits[i], toSuper(pows[i]))
print(lastresult)
print("test")
#refactor
#add comments
#build one function of that functionality
