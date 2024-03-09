from sqlalchemy import func, desc
from connect_db import session
from models import Assessment, Group, Student, Subject, Teacher

# розділювач заголовків від даних
SEP = '----------------------'

def select_1():
    result = session.query(Student.name, func.round(func.avg(Assessment.assesment), 3).label('avg_grade'))\
        .select_from(Assessment).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    
    #додаєм заголовки для таблиці
    rows = [('Студент','Середній бал'),(SEP, SEP)]
    rows.extend(result)
    return rows
 
def select_2():
    subquery1 = session.query(Subject.name).order_by(func.random()).limit(1).scalar_subquery()
    subquery2 = session.query(Student.name.label('std_name'), func.round(func.avg(Assessment.assesment), 3).label('avg_ass'), Subject.name.label('sub_name'))\
        .select_from(Student).join(Assessment).join(Subject)\
        .where(Subject.name == subquery1)\
        .group_by(Assessment.student_id, Assessment.subject_id, Student.name, Subject.name).subquery()
    result = session.query(subquery2.c.sub_name, subquery2.c.std_name, subquery2.c.avg_ass)\
        .select_from(subquery2)\
        .order_by(desc(subquery2.c.avg_ass)).limit(1).all()

    rows = [('Предмет','Студент','Макс. середній бал'),(SEP, SEP, SEP)]
    rows.extend(result)
    return rows

def select_3():
    subquery = session.query(Subject.name).order_by(func.random()).limit(1).scalar_subquery()
    result = session.query(Subject.name, Group.name, func.round(func.avg(Assessment.assesment), 3))\
        .select_from(Assessment).join(Student).join(Group).join(Subject)\
        .where(Subject.name == subquery)\
        .group_by(Group.name, Subject.name).all()

    rows = [('Предмет','Група','Середній бал'),(SEP,SEP,SEP)]
    rows.extend(result)
    return rows

def select_4():
    result = session.query(func.round(func.avg(Assessment.assesment), 3)).all()
    
    rows = [('Середній бал на потоці',),(SEP,)]
    rows.extend(result)
    return rows

def select_5():
    subquery = session.query(Teacher.name).order_by(func.random()).limit(1).scalar_subquery()
    result = session.query(Teacher.name, Subject.name)\
        .select_from(Teacher).outerjoin(Subject).where(Teacher.name == subquery).all()
    
    rows = [('Викладач','Предмет'),(SEP,SEP)]
    rows.extend(result)
    return rows

def select_6():
    subquery = session.query(Group.name).order_by(func.random()).limit(1).scalar_subquery()
    result = session.query(Group.name, Student.name)\
        .select_from(Group).join(Student).where(Group.name == subquery).all()
    
    rows = [('Група','Студент'),(SEP,SEP)]
    rows.extend(result)
    return rows

def select_7():
    subquery_gr = session.query(Group.name).order_by(func.random()).limit(1).scalar_subquery()
    subquery_su = session.query(Subject.name).order_by(func.random()).limit(1).scalar_subquery()
    result = session.query(Group.name, Subject.name, Student.name, Assessment.assesment)\
        .select_from(Group).join(Student).join(Assessment).join(Subject)\
        .filter(Group.name == subquery_gr, Subject.name == subquery_su)\
        .order_by(Student.name, Assessment.date_in)
    
    rows = [('Група','Предмет','Студент','Оцінка'),(SEP,SEP,SEP,SEP)]
    rows.extend(result)
    return rows

def select_8():
    subquery = session.query(Teacher.name).order_by(func.random()).limit(1).scalar_subquery()
    result = session.query(Teacher.name, Subject.name, func.round(func.avg(Assessment.assesment), 3))\
        .select_from(Teacher).outerjoin(Subject).outerjoin(Assessment).where(Teacher.name == subquery)\
        .group_by(Subject.id, Teacher.name)
    
    rows = [('Викладач','Предмет','Середній бал'),(SEP,SEP,SEP)]
    rows.extend(result)
    return rows

def select_9():
    subquery = session.query(Student.name).order_by(func.random()).limit(1).scalar_subquery()
    result = session.query(Student.name, Subject.name)\
        .select_from(Student).join(Assessment).join(Subject)\
        .where(Student.name == subquery)\
        .group_by(Subject.id, Student.name)
    
    rows = [('Студент','Вивчаємий предмет'),(SEP,SEP)]
    rows.extend(result)
    return rows

def select_10():
    subquery_st = session.query(Student.name).order_by(func.random()).limit(1).scalar_subquery()
    subquery_te = session.query(Teacher.name).order_by(func.random()).limit(1).scalar_subquery()
    result = session.query(Teacher.name, Student.name, Subject.name)\
        .select_from(Student).join(Assessment).join(Subject).join(Teacher)\
        .filter(Student.name == subquery_st, Teacher.name == subquery_te)\
        .group_by(Subject.id, Teacher.name, Student.name)
    print(*result)

    rows = [('Студент','Викладач','Предмет'),(SEP,SEP,SEP)]
    rows.extend(result)
    return rows