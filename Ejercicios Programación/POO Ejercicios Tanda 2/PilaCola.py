"""La pila y la cola permitirán estas operaciones:

Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.

Obtener el número de elementos almacenados (tamaño).

Saber si la pila o la cola está vacía.

Vaciar completamente la pila o la cola.


Para el caso de la pila:

Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.

Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.

Leer el elemento superior de la pila sin retirarlo (top).



Para el caso de la cola:

Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.

Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer elemento que entró.

Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front)."""


class Pila:

    def __init__(self, values=None):
        self.__size = 0
        if isinstance(values, tuple or list):
            self.__values = [x for x in values]
        elif isinstance(values, Pila):
            self.__values = [x for x in values.values]
        elif isinstance(values, Cola):
            self.__values = [x for x in values.values]
        elif values is None:
            self.__values = []
        else:
            raise ValueError(f"Formato no permitido: {values}")

    @property
    def size(self):
        return self.__size

    @property
    def values(self):
        return self.__values

    def isEmpty(self):
        if self.__size == 0:
            return True
        return False

    def clear(self):
        self.__values.clear()

    def push(self, value):
        self.__values.insert(0, value)

    def pop(self):
        return self.__values.pop(0)

    def front(self):
        return self.__values[0]


class Cola:

    def __init__(self, values=None):
        self.__size = 0
        if isinstance(values, tuple or list):
            self.__values = [x for x in values]
        elif isinstance(values, Pila):
            self.__values = [x for x in values.values]
        elif isinstance(values, Cola):
            self.__values = [x for x in values.values]
        elif values is None:
            self.__values = []
        else:
            raise ValueError(f"Formato no permitido: {values}")

    @property
    def size(self):
        return self.__size

    @property
    def values(self):
        return self.__values

    def isEmpty(self):
        if self.__size == 0:
            return True
        return False

    def clear(self):
        self.__values.clear()

    def enqueue(self, value):
        self.__values.append(value)

    def dequeue(self):
        return self.__values.pop(-1)

    def top(self):
        return self.__values[0]


if __name__ == "__main__":
    queue = Cola()
    stack = Pila()
