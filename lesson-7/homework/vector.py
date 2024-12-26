import math

class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for addition.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for subtraction.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must be of the same dimension for dot product.")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and '{}'".format(type(other).__name__))

    def __rmul__(self, other):
        return self * other

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(a / mag for a in self.components))

# Example 
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)  

v3 = v1 + v2
print(v3)  

v4 = v2 - v1
print(v4) 

dot_product = v1 * v2
print(dot_product)  

v5 = 3 * v1
print(v5)  

print(v1.magnitude())  

v_unit = v1.normalize()
print(v_unit)  