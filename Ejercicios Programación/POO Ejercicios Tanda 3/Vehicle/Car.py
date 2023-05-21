from Vehicle import Vehicle


class Car(Vehicle):

    def __init__(self):
        super().__init__()

    @staticmethod
    def burn_out():
        print("  _    _             /'_'_/.-''/                             _______\n" \
              + "  \\`../ |o_..__     / /__   / /  -= WORLD CHAMPIONSHIP =-   _\\=.o.=/_\n" \
              + "`.,(_)______(_).>  / ___/  / /                             |_|_____|_|\n" \
              + "~~~~~~~~~~~~~~~~~~/_/~~~~~/_/~~~~~~~~~~~~~~1DAW~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
              )


if __name__ == '__main__':
    Car.burn_out()
