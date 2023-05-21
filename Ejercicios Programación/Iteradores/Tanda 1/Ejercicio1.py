"""
1. Programa que recibe dos parámetros: un fichero de texto y una cadena que le indica qué información va a extraer del
mismo, después muestra por la pantalla los datos extraídos.

Los posibles valores del segundo parámetro y la información que extrae es:

DNI: extrae los DNI.
IP: extrae las direcciones IP.
MAT: extrae matrículas de coche con formato 0000XXX.
HEX: extrae números hexadecimales. Entendemos que las letras entre A y F son en mayúsculas y el número empieza con #.
FEC: extrae fechas con formato dd/mm/aaaa.
TWT: extrae usuarios de twitter: empieza por @ y puede contener letras mayúsculas y minúsculas, números, guiones y
     guiones bajos.
El programa tiene que ser en relación con su complejidad y número de líneas lo más eficiente posible.
"""

import re
result = []


def start(file, type_):

    with open(file, "rt") as f:
        content = str(f.readlines())
    match type_:
        case "DNI":
            print(dni(content))
            pass
        case "IP":
            print(ip(content))
            pass
        case "MAT":
            print(mat(content))
            pass
        case "HEX":
            print(hex_(content))
            pass
        case "FEC":
            print(fec(content))
            pass
        case "TWT":
            print(twt(content))
            pass
        case _:
            raise ValueError


def dni(content):
    global result
    result = re.findall("\d{8}[A-HJ-NP-TV-Z]", content)
    if len(result) == 0:
        result = "No se han encontrado DNIs"
    return result


def ip(content):
    global result
    result = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", content)
    if len(result) == 0:
        result = "No se han encontrado IPs"
    return result


def mat(content):
    global result
    result = re.findall("\d{4}[A-Z]{3}", content)
    if len(result) == 0:
        result = "No se han encontrado matriculas"
    return result


def hex_(content):
    global result
    result = re.findall("\#\d[A-F]?", content)
    if len(result) == 0:
        result = "No se han encontrado números hexadecimales"
    return result


def fec(content):
    global result
    result = re.findall("[1-3]?\d/[0-1]?\d/\d{4}", content) # Se come fechas erroneas como 39/17/9999
    if len(result) == 0:
        result = "No se han encontrado fechas"
    return result


def twt(content):
    global result
    result = re.findall("@\w*", content)  # Se come fechas erroneas como 39/17/9999
    if len(result) == 0:
        result = "No se han encontrado usuarios de twitter"
    return result


if __name__ == "__main__":
    start("test.txt", "DNI")
