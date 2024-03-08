from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///mylearn.db")
DBSession = sessionmaker(bind=engine)
session = DBSession()