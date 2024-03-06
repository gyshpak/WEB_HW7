from datetime import date

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import Date


Base = declarative_base()


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    groups = relationship("Group", cascade="all, delete", backref="students")
    assessments = relationship("Assessment", cascade="all, delete", backref="students")


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    subjects = relationship("Subject", cascade="all, delete", backref="teacher")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    teacher_id = Column(
        Integer, ForeignKey(Teacher.id, ondelete="CASCADE", onupdate="CASCADE")
    )
    assessments = relationship("Assessment", cascade="all, delete", backref="subjects")


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    student_id = Column(
        Integer, ForeignKey(Student.id, ondelete="CASCADE", onupdate="CASCADE")
    )


class Assessment(Base):
    __tablename__ = "assessments"
    id = Column(Integer, primary_key=True)
    assesment = Column(Integer, nullable=False)
    date_in = Column(Date, default=date.today())
    student_id = Column(Integer, ForeignKey(Student.id, ondelete="CASCADE", onupdate="CASCADE"))
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete="CASCADE", onupdate="CASCADE"))
