from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE as db

URL = f"{db['dialect']}+{db['driver']}://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}"

engine = create_engine(URL, connect_args={"check_same_thread": False}, echo=True)
# engine = <class 'sqlalchemy.engine.base.Engine'>

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
