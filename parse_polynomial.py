def parse_polynomial(inputTextPolynomial): #funckja przyjmuje wielomian w formie tekstowej w postaci "Ax^n1+Bx^n2+C"
    start = 0
    polynomialParts = []
    parsedPolynomial = {}
    for i in range(0, len(inputTextPolynomial)): #dzielimy wielomian na skladowe wzgledem znakow "+" lub "-"
        if i != 0 and inputTextPolynomial[i] == '-' or inputTextPolynomial[i] == '+':
            polynomialParts.append(inputTextPolynomial[start:i])
            start = i
        if i == len(inputTextPolynomial) - 1:
            polynomialParts.append(inputTextPolynomial[start:i+1])
    for part in polynomialParts:
        if "x^" in part:
            if part[:part.index("x")] == "":
                power = int(part[part.index("^") + 1:])
                coeff = 1
            elif part[:part.index("x")] == "-":
                power = int(part[part.index("^") + 1:])
                coeff = -1
            else:
                if "+x" in part:
                    power = int(part[part.index("^") + 1:])
                    coeff = 1
                elif "-x" in part:
                    power = int(part[part.index("^") + 1:])
                    coeff = -1
                else:
                    power = int(part[part.index("^")+1:])
                    coeff = int(part[:part.index("x")])
        elif "x" in part:
            if part == "+x":
                power = 1
                coeff = 1
            elif part == "-x":
                power = 1
                coeff = -1
            else:
                power = 1
                coeff = int(part[:part.index("x")])
        else:
            power = 0
            coeff = int(part)

        if power in parsedPolynomial:
            parsedPolynomial[power] += coeff
        else:
            parsedPolynomial[power] = coeff

    sortedParsedPolynomial = sorted(parsedPolynomial.items(), key=lambda x: x[0], reverse=True)
    return sortedParsedPolynomial

print(parse_polynomial("3x^2-2x+5"))