"""

Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО
на первую заглавную букву и наличие
только букв. Если ФИО не соответствует
условию, выведите:

    ФИО должно состоять только из букв и
    начинаться с заглавной буквы

○ Названия предметов должны загружаться
из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы.
Если такого предмета нет, выведите:

    Предмет {Название предмета} не найден

○ Для каждого предмета можно хранить
оценки (от 2 до 5) и результаты тестов
(от 0 до 100). В противном случае выведите:

    Оценка должна быть целым числом от 2 до 5

    Результат теста должен быть целым
    числом от 0 до 100

○ Также экземпляр должен сообщать средний
балл по тестам для каждого предмета и
по оценкам всех предметов вместе взятых.

Вам предоставлен файл subjects.csv,
содержащий предметы. Сейчас в файл
записана следующая информация.

    Математика,Физика,История,Литература

Создайте класс Student, который будет
представлять студента и его успехи
по предметам. Класс должен иметь
следующие методы:

    Атрибуты класса:

        name (str): ФИО студента.

        subjects (dict): Словарь,
        который хранит предметы в
        качестве ключей и информацию
        об оценках и результатах
        тестов для каждого предмета
        в виде словаря.

    Магические методы (Dunder-методы):

        __init__(self, name, subjects_file):
        Конструктор класса. Принимает имя
        студента и файл с предметами и их
        результатами. Инициализирует
        атрибуты name и subjects и
        вызывает метод load_subjects
        для загрузки предметов из файла.

        __setattr__(self, name, value):
        Дескриптор, который проверяет
        установку атрибута name.
        Убеждается, что name начинается
        с заглавной буквы и состоит
        только из букв.

        __getattr__(self, name):
        Позволяет получать значения
        атрибутов предметов (оценок
        и результатов тестов) по их именам.

        __str__(self):
        Возвращает строковое
        представление студента,
        включая имя и список предметов.

            Студент: Иван Иванов
            Предметы: Математика, История

    Методы класса:

        load_subjects(self, subjects_file):
        Загружает предметы из файла CSV.
        Использует модуль csv для чтения
        данных из файла и добавляет
        предметы в атрибут subjects.

        add_grade(self, subject, grade):
        Добавляет оценку по заданному
        предмету. Убеждается, что оценка
        является целым числом от 2 до 5.

        add_test_score(self, subject, test_score):
        Добавляет результат теста по
        заданному предмету. Убеждается,
        что результат теста является
        целым числом от 0 до 100.

        get_average_test_score(self, subject):
        Возвращает средний балл по тестам
        для заданного предмета.

        get_average_grade(self):
        Возвращает средний балл
        по всем предметам.

Пример

    На входе:

        student = Student("Иван Иванов", "subjects.csv")

        student.add_grade("Математика", 4)
        student.add_test_score("Математика", 85)

        student.add_grade("История", 5)
        student.add_test_score("История", 92)

        average_grade = student.get_average_grade()
        print(f"Средний балл: {average_grade}")

        average_test_score = student.get_average_test_score("Математика")
        print(f"Средний результат по тестам по математике: {average_test_score}")

        print(student)

    На выходе:

        Средний балл: 4.5
        Средний результат по тестам по математике: 85.0
        Студент: Иван Иванов
        Предметы: Математика, История

"""
import csv
import argparse
import logging



class FIO:

    FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" функция "{funcName}()" записала сообщение: {msg}'

    logging.basicConfig(format=FORMAT, filename='student.log.', encoding='utf-8', level=logging.ERROR, style="{")
    logger = logging.getLogger(__name__)

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')

    def validate(self, value: str):
        if not isinstance(value, str):
            err = TypeError(f'Значение {value} должно быть строкой')
            self.logger.error(err)
            raise err
            # raise TypeError(f'Значение {value} должно быть строкой')
        words = value.split()
        for word in words:
            if not word.isalpha():
                err = ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
                self.logger.error(err)
                raise err
                # raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
        if not value[0].isupper():
            err = ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")
            self.logger.error(err)
            raise err
            # raise ValueError("ФИО должно состоять только из букв и начинаться с заглавной буквы")


class Test:

    FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" функция "{funcName}()" записала сообщение: {msg}'

    logging.basicConfig(format=FORMAT, filename='student.log.', encoding='utf-8', level=logging.ERROR, style="{")
    logger = logging.getLogger(__name__)

    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value
    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    def validate(self, value):
        if not isinstance(value, int):
            err = TypeError(f'Значение {value} должно быть целым числом')
            self.logger.error(err)
            raise err
            # raise TypeError(f'Значение {value} должно быть целым числом')
        if not (0 <= value <= 100):
            err = ValueError(f"Результат теста должен быть целым числом от 0 до 100")
            self.logger.error(err)
            raise err
            # raise ValueError(f"Результат теста должен быть целым числом от 0 до 100")

class Grade:

    FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" функция "{funcName}()" записала сообщение: {msg}'

    logging.basicConfig(format=FORMAT, filename='student.log.', encoding='utf-8', level=logging.ERROR, style="{")
    logger = logging.getLogger(__name__)

    def __init__(self, min_value: int = None, max_value: int = None):
        self.min_value = min_value
        self.max_value = max_value
    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    def __delete__(self, instance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалять')
    def validate(self, value):
        if not isinstance(value, int):
            err = TypeError(f'Значение {value} должно быть целым числом')
            self.logger.error(err)
            raise err
            # raise TypeError(f'Значение {value} должно быть целым числом')
        if not (2 <= value <= 5):
            err = ValueError(f"Оценка должна быть целым числом от 2 до 5")
            self.logger.error(err)
            raise err
            # raise ValueError(f"Оценка должна быть целым числом от 2 до 5")

class Student:

    name = FIO()
    test = Test(0, 100)
    grade = Grade(2, 5)

    FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" функция "{funcName}()" записала сообщение: {msg}'

    logging.basicConfig(format=FORMAT, filename='student.log.', encoding='utf-8', level=logging.NOTSET, style="{")

    logger = logging.getLogger(__name__)


    def __init__(self, name: str, subjects):
        self.name = name
        self.logger.setLevel(logging.DEBUG)
        self.subjects = self.load_subjects(subjects)
    def __str__(self):
        return f"Студент: {self.name}\nПредметы: {', '.join(self.get_not_empty_subject())}"

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            csv_list = []
            for line in csv_file:
                csv_list.append(line)
            result = {}
            for subj in csv_list[0]:
                result[subj] = {}
        self.logger.debug(f"Предметы загружены из файла {subjects_file}")
        return result

    def add_grade(self, subject, grade):
        self.check_subj(subject)
        self.grade = grade
        self.subjects[subject]["grade"] = grade
        self.logger.debug(f"Добавлена оценка {self.subjects.get(subject).get('grade')} студенту {self.name} по предмету {subject}")

    def add_test_score(self, subject: str, test_score):
        self.check_subj(subject)
        if not self.subjects.get(subject).get("test_score"):
            self.subjects[subject]["test_score"] = []
        self.test = test_score
        self.subjects[subject]["test_score"].append(self.test)
        self.logger.debug(f"Добавлен результат тестов {self.subjects.get(subject).get('test_score')[-1]} студенту {self.name} по предмету {subject}")


    def get_average_test_score(self, subject):
        self.check_subj(subject)
        aver = self.subjects.get(subject).get("test_score")
        if isinstance(self.subjects.get(subject).get("test_score"), list):
            result = sum(aver)/len(aver)
            self.logger.debug(f"Высчитаны средние результаты {result} студента {self.name} по предмету {subject}")
            return result
        else:
            self.logger.debug(f"Результатов тестов студента {self.name} по предмету {subject} не найдено")
            return 0.0


    def get_average_grade(self):
        aver = []
        for subj in self.subjects.keys():
            if isinstance(self.subjects.get(subj).get("grade"), int):
                aver.append(self.subjects.get(subj).get("grade"))
        if aver:
            result = sum(aver)/len(aver)
            self.logger.debug(f"Высчитана средняя оценка {result} студента {self.name} по всем предметам")
            return result
        else:
            self.logger.debug(f"Оценок студента {self.name} не найдено")
            return 0.0

    def check_subj(self, subj):
        if subj not in self.subjects.keys():
            err = ValueError(f"Предмет {subj} не найден")
            self.logger.error(err)
            raise err

    def get_not_empty_subject(self):
        results = []
        for subj in self.subjects.keys():
            if len(self.subjects.get(subj)) != 0:
                results.append(subj)
        return results








if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='csv file to Student class')
    parser.add_argument("-f", metavar="f", type=str, help="write csv file with subjects")

    args = parser.parse_args()

    student = Student("Иван Иванов", args.f)
    # student = Student(123, args.f)
    # student = Student("Иван1 Иванов", args.f)
    # student = Student("иван иванов", args.f)
    # student.name = 123
    # student.name = "Иван1 Иванов"
    # student.name = "иван иванов"

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")


    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)

    student.add_grade("История", 5)
    # student.add_grade("История", 6)
    # student.add_grade("История", 4.5)
    # student.add_grade("Философия", 5)

    student.add_test_score("История", 90)
    student.add_test_score("История", 70)
    student.add_test_score("История", 41)
    # student.add_test_score("История", 102)
    # student.add_test_score("История", 90.8)
    # student.add_test_score("Философия", 90)

    average_grade = student.get_average_grade()
    print(f"Средний балл: {average_grade}")
    average_test_score = student.get_average_test_score("Математика")
    print(f"Средний результат по тестам по математике: {average_test_score}")

    # average_test_score1 = student.get_average_test_score("Философия")

    print()
    print(student)