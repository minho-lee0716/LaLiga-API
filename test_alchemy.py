from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
import sqlalchemy
from config import DATABASE as DB

print(sqlalchemy.__version__)

engine = create_engine(
    f"{DB['dialect']}+{DB['driver']}://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}",
    echo=True
)
# engine = <class 'sqlalchemy.engine.base.Engine'>

# print(engine)
# print(dir(engine))
# print(type(engine))

# print('##########')

Base = declarative_base()
# print(Base)
# print(dir(Base))
# print(type(Base))


class Club(Base):
    __tablename__ = 'clubs'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, comment='club name')
    country = Column(String(50), nullable=False, comment='club country')

    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __repr__(self):
        return "<Club('%s', '%s')>" % self.name, self.country


print(Club.__table__)
print(Club.__mapper__)

Base.metadata.create_all(engine)
