from connect_db import session
from datetime import date
from time import time
import faker
from faker.providers import DynamicProvider
from models import Assessment, Group, Student, Subject, Teacher
from random import randint, choices, choice


NUMBER_STUDENTS = randint(30, 50)
NUMBER_GROUPS = ["бджілки", "квітки", "метелики"]
NUMBER_SUBJECTS = randint(5, 8)
NUMBER_TEACHERS = randint(3, 5)


def generate_fake_data(number_students, number_subjects, number_teachers) -> tuple():
    """встановлюємо локаль"""
    fake_data = faker.Faker("uk_UA")

    """ список предметів для нового провайдера"""
    school_subject_provider = DynamicProvider(
        provider_name="school_subject",
        elements=[
            "хімія",
            "фізика",
            "алгебра",
            "анатомія",
            "історія",
            "астрономія",
            "географія",
            "інформатика",
            "культура",
            "література",
            "мова",
            "фізична культура",
        ],
    )

    """ додаєм нового провайдера для навчальних предметів"""
    fake_data.add_provider(school_subject_provider)

    fake_students = []  # тут зберігатимемо студентів
    fake_subjects = []  # тут зберігатимемо предмети
    fake_teachers = []  # тут зберігатимемо вчітелів

    """ Згенеруємо набір студентів у кількості number_students"""
    for _ in range(number_students):
        fake_students.append(fake_data.unique.name())

    """ Згенеруємо набір предметів у кількості number_subjects"""
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.unique.school_subject())

    """ Згенеруємо набір вчітелів у кількості number_teachers"""
    for _ in range(number_teachers):
        fake_teachers.append(fake_data.unique.name())

    return fake_students, fake_subjects, fake_teachers


def prepare_data(students, subjects, teachers) -> tuple():
    for_students = []
    """ готуємо список кортежів імен студентів"""
    for student in students:
        for_students.append((student,))

    for_groups = []  # для таблиці group
    for id_st in range(1, NUMBER_STUDENTS + 1):
        """
        Для записів у таблицю груп нам потрібно додати id всіх студентів.
        При створенні таблиці groups для поля id ми вказуем INTEGER AUTOINCREMENT - тому кожен запис
        отримуватиме послідовне число збільшене на 1, починаючи з 1. Рандомно розподіляємо студентів по групах.
        """
        for_groups.append((choice(NUMBER_GROUPS), id_st))

    """ готуємо список кортежів імен вітелів"""
    for_teachers = []
    for teacher in teachers:
        for_teachers.append((teacher,))

    for_subjects = []
    for subject in subjects:
        """
        Для записів у таблицю всіх предметів нам потрібно додати випадково id вчітелів.
        """
        for_subjects.append((subject, randint(1, NUMBER_TEACHERS)))

    start_date = date(year=2023, month=9, day=1)  # умовний початок навчання

    """ формуємо оцінки та їх ваги (наші студенти більш розумні ніж тупі ;-)"""
    assess = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    weights_ = [1, 2, 3, 4, 5, 5, 10, 20, 25, 15, 5, 5]

    for_assessments = []
    for id_st in range(1, NUMBER_STUDENTS + 1):
        """
        Для записів у таблицю оцінок додаєм всіх студентів, для них всі предмети(учні вчать всі предмети),
        оцінки, та дату отрамання оцінки
        """
        for id_sb in range(1, NUMBER_SUBJECTS + 1):
            for _ in range(1, randint(10, 20)):
                for_assessments.append(
                    (
                        id_st,
                        id_sb,
                        *choices(assess, weights_),
                        faker.Faker().date_between(
                            start_date=start_date, end_date="today"
                        ),
                    )
                )

    return for_students, for_groups, for_subjects, for_teachers, for_assessments


def insert_data_to_db(students, groups, subjects, teachers, assessments) -> None:
    #     """Створимо з'єднання з нашою БД та отримаємо об'єкт курсору для маніпуляцій з даними"""

    #     # with sqlite3.connect("learning.db") as con:

    #         # cur = con.cursor()

    #         """Заповнюємо таблицю студентів. І створюємо скрипт для вставлення, де змінні, які вставлятимемо, відзначимо
    #         знаком заповнювача (?) """

    #         sql_to_students = """INSERT INTO students(name_st)

    #                                        VALUES (?)"""

    #         """Для вставлення відразу всіх даних скористаємося методом executemany курсора. Першим параметром буде текст
    #         скрипта, а другим - дані (список кортежів)."""

    #         cur.executemany(sql_to_students, students)

    #         """ Далі вставляємо дані про групи."""

    #         sql_to_groups = """INSERT INTO groups(number_gr, fr_st)
    #                                VALUES (?, ?)"""

    list_stutents = []
    for i in students:
        list_stutents.append(Student(name=i[0]))
    session.add_all(list_stutents)
    session.commit()

    list_groups = []
    for i in groups:
        list_groups.append(Group(name=i[0], student_id=i[1]))
    session.add_all(list_groups)
    session.commit()

    list_teachers = []
    for i in teachers:
        list_teachers.append(Teacher(name=i[0]))
    session.add_all(list_teachers)
    session.commit()

    list_subjects = []
    for i in subjects:
        list_subjects.append(Subject(name=i[0], teacher_id=i[1]))
    session.add_all(list_subjects)
    session.commit()

    list_assessments = []
    for i in assessments:
        list_assessments.append(
            Assessment(student_id=i[0], subject_id=i[1], assesment=i[2], date_in=i[3])
        )
    session.add_all(list_assessments)
    session.commit()


#         cur.executemany(sql_to_groups, groups)

#         sql_to_teachers = """INSERT INTO teachers(name_tc)
#                                VALUES (?)"""
#         cur.executemany(sql_to_teachers, teachers)

#         sql_to_subjects = """INSERT INTO subjects(name_sb, fr_tc)
#                                VALUES (?, ?)"""
#         cur.executemany(sql_to_subjects, subjects)

#         sql_to_assessments = """INSERT INTO assessment_subj(fr_st, fr_sb, assessment, date_in)
#                               VALUES (?, ?, ?, ?)"""

#         cur.executemany(sql_to_assessments, assessments)

#         """ Фіксуємо наші зміни в БД"""

#         con.commit()

Start = time()

if __name__ == "__main__":
    students, groups, subjects, teachers, assessments = prepare_data(
        *generate_fake_data(
            NUMBER_STUDENTS,
            NUMBER_SUBJECTS,
            NUMBER_TEACHERS,
        )
    )

    insert_data_to_db(students, groups, subjects, teachers, assessments)
