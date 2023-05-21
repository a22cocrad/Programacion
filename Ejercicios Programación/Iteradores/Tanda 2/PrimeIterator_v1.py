"""
Crea el iterador PrimeIterator que permita iterar sobre la lista de números primos, desde 2 hasta uno dado como máximo.

Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]

"""


class PrimeIterator:
    def __init__(self, num: int):
        if num < 2:
            raise ValueError
        self.__list_primes = [2]
        self.__cont = 0
        self.__primes(num)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__cont + 1 == len(self.__list_primes):
            raise StopIteration
        self.__cont += 1
        return self.__list_primes[self.__cont]

    def __primes(self, num1):
        for i in range(2, num1 + 1):
            if PrimeIterator.is_prime(i):
                self.__list_primes.append(i)

    @staticmethod
    def is_prime(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


if __name__ == '__main__':
    test = list(PrimeIterator(50))
    print(test)
