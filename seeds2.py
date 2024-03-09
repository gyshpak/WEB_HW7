from connect_db import session
from datetime import date
import faker
from faker.providers import DynamicProvider
from models import Assessment, Group, Student, Subject, Teacher
from random import randint, choices, choice


def insert_data_to_db(students=None, groups=None, subjects=None, teachers=None, assessments=None) -> None:

    """Заповнюємо таблиці"""

    if students is not None:
        list_stutents = []
        for i in students:
            list_stutents.append(Student(name=i[0]))
        session.add_all(list_stutents)
        session.commit()

    if groups is not None:
        list_groups = []
        for i in groups:
            list_groups.append(Group(name=i[0], student_id=i[1]))
        session.add_all(list_groups)
        session.commit()

    if teachers is not None:
        list_teachers = []
        for i in teachers:
            list_teachers.append(Teacher(name=i[0]))
        session.add_all(list_teachers)
        session.commit()

    if subjects is not None:
        list_subjects = []
        for i in subjects:
            list_subjects.append(Subject(name=i[0], teacher_id=i[1]))
        session.add_all(list_subjects)
        session.commit()

