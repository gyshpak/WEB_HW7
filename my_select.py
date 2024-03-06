# def select_1():
#     SELECT s.fullname, round(avg(g.grade), 2) AS avg_grade
#     FROM grades g
#     LEFT JOIN students s ON s.id = g.student_id
#     GROUP BY s.id
#     ORDER BY avg_grade DESC
#     LIMIT 5;

from sqlalchemy import func
from connect_db import session
from models import Assessment, Group, Student, Subject, Teacher

def select_1():
    session.query(Student.fullname, func.round(func.avg(Assessment.assesment), 2).label('avg_grade'))\
        .select_from(Assessment).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
