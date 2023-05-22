"""
Programa para crear test usando la clase question

"""
from question import Question

questions_number = int(input("Introduce el número de preguntas que tendrá el TEST: "))
questions = []


def make_test():
    for i in range(questions_number):
        tmp_name = input(f"Ingrese el nombre para la pregunta número {i + 1}: ")
        tmp_statement = []
        while "." not in tmp_statement:
            tmp_statement.append(input(f"Ingrese el enunciado para la pregunta número {i + 1} (. para finalizar): "))
        tmp_statement = "\n".join(tmp_statement)
        tmp_answer = []
        for n in range(4):
            tmp_answer_text = input(f"Ingrese el texto para la respuesta número {n + 1}: ")
            tmp_answer_calification = float(
                input(f"Ingrese el porcentaje (entre '-1' y '+1') para la respuesta número {n + 1}: "))
            tmp_answer.append((tmp_answer_text, tmp_answer_calification))

        questions.append(Question(tmp_name, tmp_statement, tmp_answer))


def do_test():
    nota = 0
    nota_maxima = 0
    for q in range(len(questions)-1):
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


make_test()
do_test()
