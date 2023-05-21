"""
10. Crea la clase abstracta Vehicle, así como las clases Bike y Car como subclases de la primera.
Para la clase Vehicle, crea los atributos de clase vehicles_created y total_kilometers,
así como el atributo de instancia kilometers_traveled.

En la clase Vehicle crea un método para viajar (travel) que incremente los kilómetros recorridos.
En la clase Bike haz un método para hacer el caballito y en la clase Car otro para quemar rueda.

Prueba las clases creadas mediante un programa con un menú
(usando la clase de la tanda anterior) como el que se muestra a continuación:

VEHÍCULOS
=========
1. Anda con la bicicleta
2. Haz el caballito con la bicicleta
3. Anda con el coche
4. Quema rueda con el coche
5. Ver kilometraje de la bicicleta
6. Ver kilometraje del coche
7. Ver kilometraje total
8. Salir

Elige una opción (1-8):
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    __total_kilometers = 0

    def __init__(self):
        self.__kilometers = 0

    def travel(self, kilometers_to_add):
        if kilometers_to_add < 0:
            raise ValueError("Los kilómetros deben ser mayores a 0")
        Vehicle.__total_kilometers += kilometers_to_add
        self.__kilometers += kilometers_to_add

    def kilometers_traveled(self):
        return self.__kilometers

    @classmethod
    def total_kilometers_traveled(cls):
        return cls.__total_kilometers
