polynomial = "5x^22+6x^33-2x^2-x^33+x^2"
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

    # slimplifyPolynomial(pows, digits)

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
    print(list(result.keys()))
    print(wynik)




    # positions = []
    # for i in range(len(pows)):
    #     current = pows[i]
    #     positions.append(i)
    #     for j in range(len(pows)):
    #         if current == pows[j] and i != j:
    #             positions.append(j)
    #     if len(positions) >1 :
    #         temp = 0
    #         for pos in positions:
    #             if digits[pos] == "-x":
    #                 number = 1
    #             else:
    #                 number = int(digits[pos][0:-1])
    #             temp += number
    #     positions = []
    #
    # print(positions)

    return pows, digits


pows, digits = splitPolynomial(polynomial)


# def slimplifyPolynomial(pows, digits):
#     print( pows, digits)
#     current =  0
#     for i in range(len(pows)):
#         if pows[current] == pows[i]:
#             digits[i] = digits[current] + digits[i]
#         current = i
#     print(pows, digits)



def printPolynomial(pows, digits):
    superscript_dict = {
        '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴',
        '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'
    }

    lastresult = ''

    for i in range(len(pows)):
        lastresult = lastresult + "{}{}".format(digits[i], ''.join(superscript_dict[digit] for digit in str(pows[i])))
    return lastresult

#print(printPolynomial(pows, digits))







#refactor
#add comments
#build one function of that functionality
