"""
6. Crea una clase para almacenar duraciones de tiempo (Duration).
Los objetos de esta clase son intervalos de tiempo y se crean de la forma:

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

Sumar y restar objetos de la clase (el resultado es otro objeto).
Sumar y restar segundos, minutos u horas (se cambia el objeto actual).
Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10 h 35 m 5 s.
"""
from typeguard import typechecked


@typechecked
class Duration:

    def __init__(self, hours, minutes=None, seconds=None):
        if isinstance(hours, Duration):
            self.__hours, self.__minutes, self.__seconds = hours.hours, hours.minutes, hours.seconds
        elif seconds is None:
            raise ValueError("Debe introducir valores")
        elif minutes is None:
            raise ValueError("Debe introducir valores")
        else:
            self.__hours, self.__minutes, self.__seconds = hours, minutes, seconds
            self.__check_time_format()

    def __check_time_format(self):
        time_ = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        if time_ < 0:
            raise ValueError("Tiempo negativo no permitido")
        self.__hours = time_ // 3600
        time_ = time_ % 3600
        self.__minutes = time_ // 60
        self.__seconds = time_ % 60

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    def add_seconds(self, seconds: int):
        self.__seconds += seconds
        self.__check_time_format()

    def sub_seconds(self, seconds: int):
        self.__seconds -= seconds
        self.__seconds -= seconds

    def add_minutes(self, minutes: int):
        self.__minutes += minutes
        self.__check_time_format()

    def sub_minutes(self, minutes: int):
        self.__minutes -= minutes
        self.__check_time_format()

    def add_hours(self, hours: int):
        self.__hours += hours
        self.__check_time_format()

    def sub_hours(self, hours: int):
        self.__hours -= hours
        self.__check_time_format()

    def __add__(self, other: 'Duration'):
        return Duration(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def __sub__(self, other: 'Duration'):
        return Duration(self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds)

    def __str__(self):
        return f"{self.__hours} h {self.__minutes} m {self.__seconds} s"


if __name__ == '__main__':
    test = Duration(1, 20, 30)
    test2 = Duration(2, 75, -10)
    test3 = Duration(test2)
    print(test)
    print(test2)
    print(test3)
    g = (test + test2)
    print(g)
    test.add_minutes(50)
    print(test)
