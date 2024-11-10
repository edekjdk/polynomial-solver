polynomial = "5x^22-6x^33-2x^2-x-x^2-x^2"
# polynomial = input("Enter a polynomial: ")
print(polynomial)

powers = []
resta = []
def showPolynomial(polynomial):
    power = ''
    rest = ''
    for i in range(len(polynomial)):
        if polynomial[i] == '^':
            i+=1
            power=''
            while i < len(polynomial) and polynomial[i].isdigit():
                power += polynomial[i]
                i+=1
            if power:
                powers.append(power)
        else:
            rest = ''
            while i < len(polynomial) and polynomial[i] != "^":
                rest += polynomial[i]
                i+=1
            if rest:
                resta.append(rest)

showPolynomial(polynomial)
print(powers)
print(resta)
# polynomial = "5x^22-6x^33-2x^2-x-x^2-x^2"
# print(polynomial)
#
# powers = []
#
# def showPolynomial(polynomial):
#     power = ''
#     for i in range(len(polynomial)):
#         if polynomial[i] == '^':  # Jeśli napotkamy znak '^', zaczynamy szukać wykładnika
#             i += 1  # Przechodzimy do następnego znaku, który jest wykładnikiem
#             power = ''  # Resetujemy zmienną 'power', aby zebrać nowy wykładnik
#             while i < len(polynomial) and polynomial[i].isdigit():  # Zbieramy cyfry wykładnika
#                 power += polynomial[i]
#                 i += 1
#             if power:  # Jeśli wykładnik został znaleziony, dodajemy go do listy
#                 powers.append(int(power))
#
# showPolynomial(polynomial)
# print(powers)
