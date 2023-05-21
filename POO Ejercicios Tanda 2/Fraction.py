"""
7. Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador)
de forma que podamos hacer las siguientes operaciones:

Construir un objeto Fracción pasándole al constructor el numerador y el denominador.
La fracción se construye simplificada, no se puede dividir por cero.

Obtener resultado de la fracción (número real).
Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).
"""
import math
from typeguard import typechecked


@typechecked
class Fraction:

    def __init__(self, num: int, den: int):
        if den == 0:
            raise ZeroDivisionError("El denominador no puede ser 0")
        self.__num, self.__den = self.__simplify(num, den)

    @staticmethod
    def __simplify(num, den):
        gcd = math.gcd(num, den)
        num, den = num // gcd, den // gcd
        return num, den

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    @property
    def result(self):
        return self.__num / self.__den

    def __mul__(self, other: (int, 'Fraction')):
        if isinstance(other, int):
            return Fraction(self.__num * other, self.__den)
        return Fraction(self.__num * other.__num, self.__den * other.__den)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other: 'Fraction'):
        return Fraction(self.__num * other.__den, self.__den * other.__num)

    def __add__(self, other: 'Fraction'):
        return Fraction(self.__num * other.__den + self.__den * other.__num, self.__den * other.__den)

    def __sub__(self, other: 'Fraction'):
        return Fraction(self.__num * other.__den - self.__den * other.__num, self.__den * other.__den)

    def __str__(self):
        return f"{self.__num}/{self.__den}"


if __name__ == '__main__':
    test1 = Fraction(6, 12)
    print(test1)
    test2 = Fraction(4, 20)
    print(test2)
    print(test1 * 2)
    print(test1 * test2)
    print(test1 + test2)
    print(test1 - test2)
    print(test1 / test2)

