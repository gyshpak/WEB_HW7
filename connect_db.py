from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# engine = create_engine("sqlite:///mylearn.db")
engine = create_engine("postgresql://postgres:qwerty123@localhost:5432/postgres")
DBSession = sessionmaker(bind=engine)
session = DBSession()