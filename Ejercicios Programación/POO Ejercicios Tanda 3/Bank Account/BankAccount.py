"""
Implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos.
El número de cuenta se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos
con el mismo número de cuenta. La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo,
se pondrá a cero inicialmente. En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una
transferencia entre una cuenta y otra. No se permite el saldo negativo. En el siguiente capítulo se propone un
ejercicio como mejora de este, en el que se pide llevar un registro de los movimientos realizados.


Programa principal:

cuenta1 = BankAccount()
cuenta2 = BankAccount(1500)
cuenta3 = BankAccount(6000)
print(cuenta1)
print(cuenta2)
print(cuenta3)
cuenta1.deposit(2000)
cuenta2.withdraw(600)
cuenta3.deposit(75)
cuenta1.withdraw(55)
cuenta2.transfer(cuenta3, 100)
print(cuenta1)
print(cuenta2)
print(cuenta3)
Salida

Número de cta: 6942541557 Saldo: 0,00 €
Número de cta: 9319536518 Saldo: 1500,00 €
Número de cta: 7396941518 Saldo: 6000,00 €
Número de cta: 6942541557 Saldo: 1945,00 €
Número de cta: 9319536518 Saldo: 800,00 €
Número de cta: 7396941518 Saldo: 6175,00 €
"""
import random


class BankAccount:
    __accounts = []

    def __init__(self, initial_balance: int = 0):
        n = random.randint(1000000000, 9999999999)
        if n in BankAccount.__accounts or initial_balance < 0:
            raise ValueError
        self.__account_number = n
        BankAccount.__accounts.append(self.__account_number)
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if self.__account_balance + amount < 0:
            raise ValueError
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance - amount < 0:
            raise ValueError
        self.__account_balance -= amount

    def transfer(self, account, amount):
        if isinstance(account, BankAccount):
            self.__account_balance -= amount
            account.__account_balance += amount

    def __str__(self):
        return f"Número de cta: {self.__account_number} Saldo: {self.__account_balance:.2f} €"


if __name__ == '__main__':
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)