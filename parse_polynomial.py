def parse_polynomial(inputTextPolynomial): #funckja przyjmuje wielomian w formie tekstowej w postaci "Ax^n1+Bx^n2+C"
    print(inputTextPolynomial)
    start = 0
    polynomialParts = []
    for i in range(0, len(inputTextPolynomial)): #dzielimy wielomian na skladowe wzgledem znakow "+" lub "-"
        if i != 0 and inputTextPolynomial[i] == '-' or inputTextPolynomial[i] == '+':
            polynomialParts.append(inputTextPolynomial[start:i])
            start = i
        if i == len(inputTextPolynomial) - 1:
            polynomialParts.append(inputTextPolynomial[start:i])
    print(polynomialParts)
    #return inputTextPolynomial