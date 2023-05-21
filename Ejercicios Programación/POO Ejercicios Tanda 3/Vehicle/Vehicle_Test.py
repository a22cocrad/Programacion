from Menu import *
from Car import Car
from Bike import Bike
from Vehicle import Vehicle

my_bike = Bike()
my_car = Car()


def main():
    menu = Menu("Anda con la bicicleta", "Haz el caballito con la bicicleta", "Anda con el coche",
                "Quema rueda con el coche", "Ver kilometraje de la bicicleta", "Ver kilometraje del coche",
                "Ver kilometraje total", "Salir", title="VEHÍCULOS")
    while True:
        opc = menu.choose()
        match opc:
            case 1:
                bike_travel(int(input("Introduce los kilómetros: ")))
            case 2:
                my_bike.wheelie()
            case 3:
                car_travel(int(input("Introduce los kilómetros: ")))
            case 4:
                my_car.burn_out()
            case 5:
                bike_kilometers()
            case 6:
                car_kilometers()
            case 7:
                total_kilometers()
            case _:
                break


def bike_travel(km):
    my_bike.travel(km)


def car_travel(km):
    my_car.travel(km)


def bike_kilometers():
    print(my_bike.kilometers_traveled())


def car_kilometers():
    print(my_car.kilometers_traveled())


def total_kilometers():
    print(Vehicle.total_kilometers_traveled())


if __name__ == '__main__':
    main()