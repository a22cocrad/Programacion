from typeguard import typechecked


@typechecked
class Question:
    def __init__(self, name: str, statement: str, answers: list[list[str, float]], score: float = 1):
        self.__name = name
        self.__statement = statement
        self.__answers = answers
        self.__score = score

    def reply(self, answers: str):
        for i in self.__answers:
            if answers in i[0]:
                return i[1] * self.__score
        raise ValueError("Respuesta no válida")

    @property
    def name(self):
        return self.__name

    @property
    def statement(self):
        return self.__statement

    @property
    def answers(self):
        return self.__answers

    @property
    def score(self):
        return self.__score

    @property
    def correct_answer(self):
        for i in self.__answers:
            if i[1] + 1:
                return i[0]
