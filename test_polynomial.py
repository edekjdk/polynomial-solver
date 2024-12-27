import unittest

from main import result
from parse_polynomial import parse_polynomial
from polynomial import Polynomial


#print(parse_polynomial(textPolynomial1))
class TestPolynomial:

    #def test(capsys):
        # #try
        # textPolynomial1 = "3x^2-2x+5"
        #
        # poly1 = Polynomial(parse_polynomial(textPolynomial1))
        # #when
        # poly1.print()
        # out, err = capsys.readouterr()
        #
        # #then
        # assert out == "3x²-2x+5\n"

    def test_parse_polynomial(self):
        #try
        textPolynomial = "3x^2-2x+5"

        #when
        parsed = parse_polynomial(textPolynomial)

        assert parsed == [(2, 3), (1, -2), (0, 5)]

    def test_polynomial_print(self, capsys):
        textPolynomial = "3x^2-2x+5"
        parsed = parse_polynomial(textPolynomial)
        poly = Polynomial(parsed)
        result = poly.print()

        assert result == "3x²-2x+5"
        '''
        parsed = parse_polynomial(textPolynomial)

        poly = Polynomial(parsed)
        poly.print()

        out, err = capsys.readouterr()

        assert out == "3x²-2x+5\n"
        '''
    def test_polynomial_free_term(self, capsys):
        textPolynomial = "5"
        parsed = parse_polynomial(textPolynomial)

        poly = Polynomial(parsed)
        result = poly.print()

        #out, err = capsys.readouterr()
        #assert out == "5\n"

        assert result == "5"

    def test_parse_polynomial_free(self):
        #try
        textPolynomial = ""

        #when
        parsed = parse_polynomial(textPolynomial)

        assert parsed == []


    def test_polynomial_degree(self, capsys):
        textPolynomial = "x^100-x^99"
        parsed = parse_polynomial(textPolynomial)

        poly = Polynomial(parsed)
        result = poly.degree()
        # out, err = capsys.readouterr()
        #
        # assert out == "100\n"
        assert result == 100

    # def test_polynomial_value(self, capsys):
    #     textPolynomial = "x^2+2x+1"
    #     parsed = parse_polynomial(textPolynomial)
    #     poly = Polynomial(parsed)
    #
    #     poly.value(1)
    #     out, err = capsys.readouterr()
    #
    #     assert out == "4\n"