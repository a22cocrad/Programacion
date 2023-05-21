"""
8. Muestra un menú con las siguientes opciones:

Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa.
Si no se introduce correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.

Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor.
Si el número es negativo restará los días. Esta opción sólo podrá realizarse si hay una fecha introducida
(se ha ejecutado la opción anterior), si no la hay mostrará un mensaje de error.

Añadir meses a la fecha. El mismo procedimiento que la opción anterior.

Añadir años a la fecha. El mismo procedimiento que la opción 2.

Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da error)
y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior,
igual o posterior a la que tenemos almacenada y el número de días comprendido entre las dos fechas.

Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").

Terminar.

Consideraciones a tener en cuenta:

Las fechas las manejaremos con la clase datetime.date.
"""
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

from Menu import Menu

date_ = None


def main():
    menu = Menu("Introducir una fecha", "Añadir dias a la fecha", "Añadir meses a la fecha",
                "Añadir años a la fecha", "Comparar fechas", "Mostrar fecha", "Salir", title="Menu para fechas")
    while True:
        opc = menu.choose()
        if opc != 1 and date_ is None and opc != menu.last_option:
            print("Debes introducir primero una fecha\n")
            continue
        match opc:
            case 1:
                option_1()
            case 2:
                option_2()
            case 3:
                option_3()
            case 4:
                option_4()
            case 5:
                option_5()
            case 6:
                option_6()
            case _:
                break


def option_1():
    global date_
    date_str = input("Introduzca una fecha en formato dd/mm/aaaa: ")
    date_ = datetime.strptime(date_str, "%d/%m/%Y").date()


def option_2():
    global date_
    days_to_add = int(input("Introduce los días a añadir: "))
    date_ += relativedelta(days=days_to_add)


def option_3():
    global date_
    months_to_add = int(input(f"Introduce los meses a añadir: "))
    date_ += relativedelta(months=months_to_add)


def option_4():
    global date_
    years_to_add = int(input(f"Introduce los años a añadir: "))
    date_ += relativedelta(years=years_to_add)


def option_5():
    global date_
    date_to_compare_str = input("Introduzca una fecha para comparar con la almacenada en formato dd/mm/aaaa: ")
    date_to_compare = datetime.strptime(date_to_compare_str, "%d/%m/%Y").date()
    if date_to_compare < date_:
        print("La fecha introducida es menor que la fecha almacenada.")
    elif date_to_compare == date_:
        print("La fecha introducida es igual a la fecha almacenada.")
    else:
        print("La fecha introducida es mayor que la fecha almacenada.")


def option_6():
    print(date_.strftime("%A, %d de %B de %Y"))


if __name__ == '__main__':
    main()
