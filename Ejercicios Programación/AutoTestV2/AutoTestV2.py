"""
Programa para crear test usando la clase question

"""
from POO.Menu.menu import Menu
from question import Question
import json

questions = []


def make_test():
    questions_number = int(input("Introduce el número de preguntas que tendrá el TEST: "))

    for i in range(questions_number):
        tmp_name = input(f"Ingrese el nombre para la pregunta número {i + 1}: ")
        tmp_statement = []
        while "." not in tmp_statement:
            tmp_statement.append(input(f"Ingrese el enunciado para la pregunta número {i + 1} (. para finalizar): "))
        tmp_statement = "\n".join(tmp_statement)
        tmp_answer = []
        for n in range(4):
            tmp_answer_text = input(f"Ingrese el texto para la respuesta número {n + 1}: ")
            tmp_answer_qualification = float(
                input(f"Ingrese el porcentaje (entre '-1' y '+1') para la respuesta número {n + 1}: "))
            tmp_answer.append((tmp_answer_text, tmp_answer_qualification))

        questions.append(Question(tmp_name, tmp_statement, tmp_answer))


def do_test():
    nota = 0
    nota_maxima = 0
    for q in range(len(questions)):
        actual = questions[q]
        print(f"Pregunta {q + 1}. \n {actual.statement}")
        for f in range(len(actual.answers)):
            print(f"{f + 1}. {actual.answers[f][0]}")
        input_value = int(input("Indique la opción correcta (Pulse Intro para dejarla en blanco): "))
        print("\n")
        if 0 < input_value <= len(actual.answers):
            nota += actual.answers[input_value-1][1] * actual.score
        nota_maxima += actual.score
    print(f"Puntuación obtenida: {(nota * 10) / nota_maxima} puntos.\n\n")


def load_test():
    global questions
    questions = []

    f_name = input("Ingrese el nombre del fichero desde el que cargar el test: ")
    with open(f_name, "rt", encoding="UTF-8") as f:
        f_json = json.load(f)

        for i in f_json:
            questions.append(Question(i["name"], i["statement"], i["options"], i["points"]))


def save_test():
    f_name = input("Ingrese el nombre del fichero donde guardar el test: ")
    raw_questions = []
    for n in questions:
        raw_questions.append({"name": n.name, "statement": n.statement, "options": n.answers, "points": n.score})
    with open(f_name, "wt", encoding="UTF-8") as f:
        f.write(json.dumps(raw_questions, indent=3, ensure_ascii=True))
    print("\n")


if __name__ == "__main__":
    options = ("Crear Nuevo Test", "Cargar Test desde Archivo", "Guardar Test actual en Archivo", "Realizar Test")
    m = Menu("AutoTest V2", options)
    switch = False
    while True:
        selected = m.print_menu()

        match selected:
            case 0:
                break
            case 1:
                make_test()
                switch = True
            case 2:
                if switch:
                    confirmation = input("Se eliminarán las preguntas guardadas, ¿desea continuar? (S/N): ")
                    if confirmation.upper() == "S":
                        load_test()
                else:
                    load_test()
                    switch = True
            case 3:
                if switch:
                    save_test()
                else:
                    print("No hay ninguna pregunta guardada.")
            case 4:
                if switch:
                    do_test()
                else:
                    print("No hay ninguna pregunta guardada.")
