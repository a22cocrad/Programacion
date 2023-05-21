"""
Haz el ejercicio anterior usando una lista interna y eliminando elementos con el algoritmo de la criba de Eratóstenes.
"""


class PrimeIteratorWithEratostenes:
    def __init__(self, num: int):
        if num < 2:
            raise ValueError
        self.__number_received = num
        self.__numbers = [number for number in range(2, num + 1)]
        self.__new_number = []
        self.__to_add = [2]
        self.Eratostenes(2)

    def Eratostenes(self, num):
        for number in self.__numbers:
            if number % num != 0:
                self.__new_number.append(number)
        self.__numbers = self.__new_number.copy()
        self.__new_number.clear()
        if self.__numbers[0] ** 2 < self.__number_received:
            self.__to_add.append(self.__numbers[0])
            self.Eratostenes(self.__numbers[0])
            return self.__numbers
        else:
            for i in self.__to_add:
                self.__numbers.append(i)
            self.__numbers.sort()

    def __iter__(self):
        return self

    @property
    def numbers(self):
        return self.__numbers


if __name__ == '__main__':
    test = (PrimeIteratorWithEratostenes(50))
    print(test.numbers)


