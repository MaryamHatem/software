import math

class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imaginary = imaginary_part

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real:.2f} + {self.imaginary:.2f}i"
        else:
            return f"{self.real:.2f} - {-self.imaginary:.2f}i"

    def __add__(self, other):
        real_sum = self.real + other.real
        imaginary_sum = self.imaginary + other.imaginary
        return ComplexNumber(real_sum, imaginary_sum)

    def __sub__(self, other):
        real_diff = self.real - other.real
        imaginary_diff = self.imaginary - other.imaginary
        return ComplexNumber(real_diff, imaginary_diff)

    def __mul__(self, other):
        real_prod = self.real * other.real - self.imaginary * other.imaginary
        imaginary_prod = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_prod, imaginary_prod)
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        real_div = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_div = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_div, imaginary_div)
    def mod(self):
        magnitude = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return round(magnitude, 2)

# Example usage
c_real = float(input("Enter the real part of complex number c: "))
c_imaginary = float(input("Enter the imaginary part of complex number c: "))
d_real = float(input("Enter the real part of complex number d: "))
d_imaginary = float(input("Enter the imaginary part of complex number d: "))

c = ComplexNumber(c_real, c_imaginary)
d = ComplexNumber(d_real, d_imaginary)

print("c + d =", c + d)
print("c - d =", c - d)
print("c * d =", c * d)
print("c / d =", c / d)
print("|c| =", c.mod())
print("|d| =", d.mod())

