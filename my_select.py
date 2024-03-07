from sqlalchemy import func, desc
from connect_db import session
from models import Assessment, Group, Student, Subject, Teacher

def select_1():
    result = session.query(Student.name, func.round(func.avg(Assessment.assesment), 3).label('avg_grade'))\
        .select_from(Assessment).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

    # stmt = (
    #     select(Student.name, func.round(func.avg(Assessment.assesment), 3).label('avg_grade')) from(Assessment).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all())
    
    return(result)
 
def select_2():
    """
    SELECT std.name_st as student, AVG(ass.assessment) as max_sred_assessment, sub.name_sb as subject
    FROM students std
    JOIN assessment_subj ass ON std.id_st = ass.fr_st
    JOIN subjects sub ON ass.fr_sb = sub.id_sb 
    WHERE sub.id_sb = (SELECT sub2.id_sb FROM subjects sub2 ORDER BY RANDOM() LIMIT 1)
    GROUP BY ass.fr_st , ass.fr_sb
    ORDER BY max_sred_assessment
    DESC 
    LIMIT 1
    """
    pass
    # result = session.query(Student.name, func.random(func.avg(Assessment.assesment), 3).label('avg_assessment'), Subject.name)\
    #                        .select_from(Student).join(Assessment).join(Subject)\
    #                         .where(Subject.id == scalar())
    

def select_3():
    subquery = session.query(Subject.name).order_by(func.random()).scalar_subquery()
    result = session.query(Group.name, func.round(func.avg(Assessment.assesment), 3).label("avg_assessment"), Subject.name)\
        .select_from(Assessment).join(Student).join(Group).join(Subject).where(Subject.name == subquery).group_by(Group.id)
    return result

def select_4():
    result = session.query(func.round(func.avg(Assessment.assesment), 3))
    return result

def select_5():
    subquery = session.query(Teacher.name).order_by(func.random()).scalar_subquery()
    result = session.query(Teacher.name, Subject.name)\
        .select_from(Teacher).outerjoin(Subject).where(Teacher.name == subquery)
    return result


def select_6():
    subquery = session.query(Group.name).order_by(func.random()).scalar_subquery()
    result = session.query(Group.name, Student.name)\
        .select_from(Group).join(Student).where(Group.name == subquery)
    return result

def select_7():
    subquery_gr = session.query(Group.name).order_by(func.random()).scalar_subquery()
    subquery_su = session.query(Subject.name).order_by(func.random()).scalar_subquery()
    result = session.query(Group.name, Subject.name, Student.name, Assessment.assesment)\
        .select_from(Group).join(Student).join(Assessment).join(Subject)\
        .filter(Group.name == subquery_gr, Subject.name == subquery_su)
    return result


def select_8():
    pass

def select_9():
    pass

def select_10():
    pass