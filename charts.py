

class Charts:
    @staticmethod
    def draw_chart(*args):
        for w in args:
            print(w.poly, w.degree())
