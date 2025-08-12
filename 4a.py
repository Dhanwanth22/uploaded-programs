 
class polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __str__(self):
        if not self.coeffs or all(coeff == 0 for coeff in self.coeffs.values()):
            return "0"

        terms = []
        for exp in sorted(self.coeffs.keys(), reverse=True):
            coeff = self.coeffs[exp]
            if coeff == 0:
                continue

            if exp == 0:
                term = "{}".format(coeff)
            elif exp == 1:
                if coeff == 1:
                    term = "x"
                elif coeff == -1:
                    term = "-x"
                else:
                    term = "{}x".format(coeff)
            else:
                if coeff == 1:
                    term = "x^{}".format(exp)
                elif coeff == -1:
                    term = "-x^{}".format(exp)
                else:
                    term = "{}x^{}".format(coeff, exp)
            terms.append(term)

        polynomial_str = terms[0]
        for term in terms[1:]:
            if term.startswith('-'):
                polynomial_str += " - " + term[1:]
            else:
                polynomial_str += " + " + term
        return polynomial_str


# Example usage:
poly = polynomial({3: 1, 2: -1, 1: 2, 0: -5})
print(poly)
