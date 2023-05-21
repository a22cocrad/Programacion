"""
Implementa la clase Terminal. Un terminal tiene asociado un número de teléfono.
Los terminales se pueden llamar unos a otros y el tiempo de conversación corre para ambos.
A continuación se proporciona el contenido del programa principal que usa esta clase y el resultado que debe
aparecer por pantalla. Los números de teléfono tienen que validarse como tales al crear el objeto (solo dígitos,
empiezan por 9, 6 o 7, su longitud es de nueve dígitos) y no puede haber dos terminales con el mismo número.

Programa principal:

t1 = Terminal("678112233")
t2 = Terminal("644744469")
t3 = Terminal("622328909")
t4 = Terminal("664739818")
print(t1)
print(t2)
t1.call(t2, 320)
t1.call(t3, 200)
print(t1)
print(t2)
print(t3)
print(t4)
Salida:

No 678 11 22 33 - 0s de conversación
No 644 74 44 69 - 0s de conversación
No 678 11 22 33 - 520s de conversación
No 644 74 44 69 - 320s de conversación
No 622 32 89 09 - 200s de conversación
No 664 73 98 18 - 0s de conversación
"""


class Terminal:
    __numbers = []

    def __init__(self, num: str):
        if num[0] in "679" and num.isdigit() and len(num) == 9 and num not in Terminal.__numbers:
            self.__number = num
            Terminal.__numbers.append(num)
            self.__talked_time = 0
        else:
            raise ValueError

    def call(self, other: 'Terminal', time: int):
        if time < 0:
            raise ValueError("El tiempo debe ser mayor a 0")
        if self.__number == other.__number:
            raise ValueError("No puede llamarse a si mismo")
        self.__talked_time += time
        other.__talked_time += time

    def __str__(self):
        return self.__number[:3] + " " + self.__number[3:5] + " " + self.__number[5:7] + " " + self.__number[7:9] + \
            f" {self.__talked_time}s de conversación"


if __name__ == '__main__':
    t1 = Terminal("678112233")
    t2 = Terminal("644744469")
    t3 = Terminal("622328909")
    t4 = Terminal("664739818")

    print(t1)
    print(t2)
    t1.call(t2, 320)
    t1.call(t3, 200)
    print(t1)
    print(t2)
    print(t3)
    print(t4)
