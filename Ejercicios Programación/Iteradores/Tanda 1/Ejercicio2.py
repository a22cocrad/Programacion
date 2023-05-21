"""
2. Programa que reciba una url y el nombre de una etiqueta html. Si la url es válida debe mostrar por la pantalla el
contenido de cada etiqueta.

Ejemplo:

sí ejecuto python miprograma https://www.iesgrancapitan.org/ title

La salida sería:

Centro Educativo IES Gran Capitán

Número de etiquetas encontradas: 1

o sí ejecuto python miprograma https://example.com/ p

La salida sería:

This domain is for use in illustrative examples in documents. You may use this domain in literature without prior
coordination or asking for permission.


<a href="https://www.iana.org/domains/example">More information...</a>

Número de etiquetas encontradas: 2
"""

import re
import requests


def start(url: str, tag: str):
    if __check_valid_url(url) is None:
        raise ValueError("URL No válida.")
    html = requests.get(url)
    source = html.text
    __find_tags_content(source, tag)


def __check_valid_url(url):
    url_types = ["^http://", "^https://", "^ftp://", "^file://"]
    for i in url_types:
        if re.match(i, url) is not None:
            return re.match(i, url)
    return None


def __find_tags_content(source, tag):
    result = re.findall(f"<{tag}>(.*)\n*(.*)</{tag}>", source)
    print(result)
    print(f"Número de etiquetas encontradas: {len(result)}")


if __name__ == "__main__":
    start("https://example.org", "p")
