from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
import sqlalchemy
from config import DATABASE as DB

print(sqlalchemy.__version__)  # 1.4.26

engine = create_engine(
    f"{DB['dialect']}+{DB['driver']}://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}",
    echo=True
)
# engine = <class 'sqlalchemy.engine.base.Engine'>

# print(engine)
# print(dir(engine))
# print(type(engine))

Base = declarative_base()
# print(Base)
# print(dir(Base))
# print(type(Base))


class Stadium(Base):
    __tablename__ = "stadiums"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, comment="Stadium Name")
    created_at = Column(DATE, nullable=True, server_default=None, comment="Completion Date")

    def __init__(self, name, created_at=None):
        self.name = name
        self.created_at = created_at

    # def __init__(self, created_at):
    #     self.created_at = None

    def __repr__(self):
        return "<Stadium('%s')>" % self.name


class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, comment="Club Name")
    stadium_id = Column(
        ForeignKey("stadiums.id", ondelete="SET NULL", onupdate="CASCADE"),
        nullable=True,
        server_default=None,
        comment="Stadium Reference ID"
    )

    def __init__(self, name, stadium_id=None):
        self.name = name
        self.stadium_id = stadium_id

    def __repr__(self):
        return "<Club('%s')>" % self.name


print(Club.__table__)  # clubs
print(Club.__mapper__)  # mapped class Club->clubs

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# print(Stadium())
# print(Club())

stadium = Stadium('Santiago Bernabeu')
print(stadium)  # Santiago Bernabeu
print(stadium.id)  # None
session.add(stadium)
session.commit()
print(stadium.id)  # 1

club = Club('Real Madrid', stadium.id)
print(club)  # Real Madrid
print(club.id)  # None
print(club.stadium_id)  # 1
session.add(club)
session.commit()
print(club.id)  # 1
print(club.stadium_id)  # 1
