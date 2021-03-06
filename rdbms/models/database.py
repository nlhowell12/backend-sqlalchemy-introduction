import os

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker()
Session.configure(bind=engine.connect())