from sqlalchemy import func, desc, Result
from connect_db import session
from models import Assessment, Group, Student, Subject, Teacher

def select_1():
    result = session.query(Student.name, func.round(func.avg(Assessment.assesment), 3).label('avg_grade'))\
        .select_from(Assessment).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

    rows = [('Студент','Середній бал'),('----------------------','----------------------')]
    rows.extend(result)
    
    return rows
    
    # return(result)
 
def select_2():
    pass
    

def select_3():
    subquery = session.query(Subject.name).order_by(func.random()).scalar_subquery()
    result = session.query(Subject.name, Group.name, func.round(func.avg(Assessment.assesment), 3))\
        .select_from(Assessment).join(Student).join(Group).join(Subject).where(Subject.name == subquery).group_by(Group.name).all()

    rows = [('Предмет','Група','Середній бал'),('----------------------','----------------------','----------------------')]
    rows.extend(result)
    
    return rows

def select_4():
    result = session.query(func.round(func.avg(Assessment.assesment), 3)).all()
    
    rows = [('Середній бал на потоці',),('----------------------',)]
    rows.extend(result)
    
    return rows

def select_5():
    subquery = session.query(Teacher.name).order_by(func.random()).scalar_subquery()
    result = session.query(Teacher.name, Subject.name)\
        .select_from(Teacher).outerjoin(Subject).where(Teacher.name == subquery).all()
    
    rows = [('Викладач','Предмет'),('----------------------','----------------------')]
    rows.extend(result)
    
    return rows


def select_6():

    subquery = session.query(Group.name).order_by(func.random()).scalar_subquery()
    result = session.query(Group.name, Student.name)\
        .select_from(Group).join(Student).where(Group.name == subquery).all()
    
    rows = [('Група','Студент'),('----------------------','----------------------')]
    rows.extend(result)
    
    return rows

def select_7():
    subquery_gr = session.query(Group.name).order_by(func.random()).scalar_subquery()
    subquery_su = session.query(Subject.name).order_by(func.random()).scalar_subquery()
    result = session.query(Group.name, Subject.name, Student.name, Assessment.assesment)\
        .select_from(Group).join(Student).join(Assessment).join(Subject)\
        .filter(Group.name == subquery_gr, Subject.name == subquery_su)\
        .order_by(Student.name, Assessment.date_in)
    
    rows = [('Група','Предмет','Студент','Оцінка'),('----------------------','----------------------','----------------------','----------------------')]
    rows.extend(result)
    
    return rows


def select_8():
    subquery = session.query(Teacher.name).order_by(func.random()).scalar_subquery()
    result = session.query(Teacher.name, Subject.name, func.round(func.avg(Assessment.assesment), 3))\
        .select_from(Teacher).outerjoin(Subject).outerjoin(Assessment).where(Teacher.name == subquery).group_by(Subject.id)
    
    rows = [('Викладач','Предмет','Середній бал'),('----------------------','----------------------','----------------------')]
    rows.extend(result)
    
    return rows

def select_9():
    subquery = session.query(Student.name).order_by(func.random()).scalar_subquery()
    result = session.query(Student.name, Subject.name)\
        .select_from(Student).join(Assessment).join(Subject)\
        .where(Student.name == subquery).group_by(Subject.id)
    
    rows = [('Студент','Вивчаємий предмет'),('----------------------','----------------------')]
    rows.extend(result)
    
    return rows

def select_10():
    subquery_st = session.query(Student.name).order_by(func.random()).scalar_subquery()
    subquery_te = session.query(Teacher.name).order_by(func.random()).scalar_subquery()
    result = session.query(Teacher.name, Student.name, Subject.name)\
        .select_from(Student).join(Assessment).join(Subject).join(Teacher)\
        .filter(Student.name == subquery_st, Teacher.name == subquery_te)\
        .group_by(Subject.id)
    print(*result)

    rows = [('Студент','Викладач','Предмет'),('----------------------','----------------------','----------------------')]
    rows.extend(result)
    
    return rows