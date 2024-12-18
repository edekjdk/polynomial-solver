def parse_polynomial(inputTextPolynomial): #funckja przyjmuje wielomian w formie tekstowej w postaci "Ax^n1+Bx^n2+C"
    print(inputTextPolynomial)
    start = 0
    polynomialParts = []
    parsedPolynomial = {}
    for i in range(0, len(inputTextPolynomial)): #dzielimy wielomian na skladowe wzgledem znakow "+" lub "-"
        if i != 0 and inputTextPolynomial[i] == '-' or inputTextPolynomial[i] == '+':
            polynomialParts.append(inputTextPolynomial[start:i])
            start = i
        if i == len(inputTextPolynomial) - 1:
            polynomialParts.append(inputTextPolynomial[start:i+1])
    print(polynomialParts)
    for part in polynomialParts:
        if "x^" in part:
            power = int(part[part.index("^"):])
            coeff = part[:part.index("x")]
            if "+" in coeff:
                coeff = int(coeff[coeff.index("+"):])
            print(power, coeff)
        elif "x" in part:
            power = 1
            coeff = part[:part.index("x")]
            if "+" in coeff:
                coeff = int(coeff[coeff.index("+") + 1:])
            if len(part) == 2:
                power = 1
                coeff = 1
        else:
            power = 0
            coeff = int(part)

        if power in parsedPolynomial:
            parsedPolynomial[power] += coeff
        else:
            parsedPolynomial[power] = coeff
    return parsedPolynomial
    #print(polynomialParts) #tablica z czesciami wielomianu
    #return inputTextPolynomial