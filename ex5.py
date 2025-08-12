def input_polynomial():
    """
    Input a polynomial from the user.
    Returns a dictionary with exponent as key and coefficient as value.
    """
    poly = {}
    n = int(input("Enter number of terms in the polynomial: "))
    print("Enter each term as: coefficient exponent")
    for _ in range(n):
        coeff, exp = map(int, input("Term: ").split())
        poly[exp] = poly.get(exp, 0) + coeff
    return poly


def add_polynomials(p1, p2):
    """
    Add two polynomials represented as dictionaries.
    """
    result = p1.copy()
    for exp, coeff in p2.items():
        result[exp] = result.get(exp, 0) + coeff
    return result


def display_polynomial(poly):
    """
    Display the polynomial in readable format.
    """
    if not poly:
        print("0")
        return

    terms = []
    for exp in sorted(poly.keys(), reverse=True):
        coeff = poly[exp]
        if coeff == 0:
            continue
        term = "{coeff}" if exp == 0 else "{coeff}x^{exp}" if exp != 1 else "{coeff}x"
        terms.append(term)
    print(" + ".join(terms))


# Main execution
print("Enter the first polynomial:")
poly1 = input_polynomial()

print("\nEnter the second polynomial:")
poly2 = input_polynomial()

result = add_polynomials(poly1, poly2)

print("\nResultant Polynomial after Addition:")
display_polynomial(result)
