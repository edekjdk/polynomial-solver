class Polynomial:
    def __init__(self, poly):
        self.poly = poly

    def print(self):
        print(self.poly)



poly1 = Polynomial("2x^2-x")
poly1.print()