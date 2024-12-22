class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    @property
    def degree(self):
        return len(self.coefficients) - 1

    def __repr__(self):
        terms = []
        for i, coeff in enumerate(self.coefficients):
            if coeff != 0:
                term = f"{coeff}x^{i}" if i > 0 else f"{coeff}"
                terms.append(term)
        return " + ".join(terms)

    def __call__(self, x):
        result = 0
        for i, coeff in enumerate(self.coefficients):
            result += coeff * x ** i
        return result

    def __add__(self, other):
        if len(self.coefficients) > len(other.coefficients):
            longer = self.coefficients[:]
            shorter = other.coefficients
        else:
            longer = other.coefficients[:]
            shorter = self.coefficients

        for i, coeff in enumerate(shorter):
            longer[i] += coeff

        return Polynomial(longer)

    def __sub__(self, other):
        if len(self.coefficients) > len(other.coefficients):
            longer = self.coefficients[:]
            shorter = other.coefficients
        else:
            longer = [-x for x in other.coefficients]
            shorter = self.coefficients

        for i, coeff in enumerate(shorter):
            longer[i] += coeff

        return Polynomial(longer)

    def __mul__(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, self_coeff in enumerate(self.coefficients):
            for j, other_coeff in enumerate(other.coefficients):
                result[i + j] += self_coeff * other_coeff
        return Polynomial(result)

    def derivative(self):
        new_coeffs = [i * coeff for i, coeff in enumerate(self.coefficients)]
        return Polynomial(new_coeffs[1:])

# Примеры использования
P1 = Polynomial([3, 2, 1])
P2 = Polynomial([1, -1, 0])

print(f"P1: {P1}")
print(f"P2: {P2}")

print(f"P1 + P2: {P1 + P2}")
print(f"P1 - P2: {P1 - P2}")
print(f"P1 * P2: {P1 * P2}")

print(f"P1(2): {P1(2)}")
print(f"P1 derivative: {P1.derivative()}")
