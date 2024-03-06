# from sqlalchemy.engine import create_engine
# create_engine
# from sqlalchemy.orm import sessionmaker

# engine = create_engine("sqlite:///mylearn.db")
# Session = sessionmaker(bind=engine)
# session = Session()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine("sqlite:///mylearn.db")
DBSession = sessionmaker(bind=engine)
session = DBSession()
