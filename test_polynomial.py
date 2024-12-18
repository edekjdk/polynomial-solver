# import unittest
# from polynomial import Polynomial
# from parse_polynomial import parse_polynomial
#
#
# class TestPolynomial(unittest.TestCase):
#     def test_parse_polynomial(self):
#         # Test poprawnego parsowania
#         parsed = parse_polynomial("3x^2-2x+5")
#         expected = [(2, 3), (1, -2), (0, 5)]  # [(power, coefficient)]
#         self.assertEqual(parsed, expected)
#
#     def test_polynomial_print(self):
#         # Test poprawnego wyświetlania
#         poly = Polynomial([(2, 3), (1, -2), (0, 5)])  # 3x^2 - 2x + 5
#         self.assertEqual(str(poly), "3x²-2x+5")
#
#     def test_polynomial_free_term(self):
#         # Test wielomianu z samym wyrazem wolnym
#         poly = Polynomial([(0, 5)])  # 5
#         self.assertEqual(str(poly), "5")
#
#     def test_empty_polynomial(self):
#         # Test pustego wielomianu
#         parsed = parse_polynomial("")
#         self.assertEqual(parsed, [])
#
#
# if __name__ == "__main__":
#     unittest.main()
# test_polynomial.py
from polynomial import Polynomial
from parse_polynomial import parse_polynomial

textPolynomial1 = "3x^2-2x+5"

parsed = parse_polynomial(textPolynomial1)
print("Parsed Polynomial:", parsed)  # Oczekiwany wynik: [(2, 3), (1, -2), (0, 5)]

poly = Polynomial(parsed)
print(poly.print())  # Oczekiwany wynik: "3x²-2x+5"
