from sqlalchemy import Column, DATE, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


# class Stadium(Base):
#     __tablename__ = "stadiums"
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False, comment="Stadium Name")
#     created_at = Column(DATE, nullable=True, default=None, comment="Completion Date")
#     # created_at = Column(DATE, nullable=True, server_default=None, comment="Completion Date")
#
#     club = relationship("Club", back_populates="stadium", uselist=False)


class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, comment="Club Name")
    # stadium_id = Column(
    #     ForeignKey("stadiums.id", ondelete="SET NULL", onupdate="CASCADE"),
    #     nullable=True,
    #     default=None,
    #     # server_default=None,
    #     comment="Stadium Reference ID"
    # )

    # stadium = relationship("Stadium", back_populates="club")
    players = relationship("Player", back_populates="club")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, comment="Player Name")
    back_number = Column(Integer, nullable=True, default=None, comment="Player Back Number")
    club_id = Column(
        ForeignKey("clubs.id", ondelete="SET NULL", onupdate="CASCADE"),
        nullable=True,
        default=None,
        # server_default=None,
        comment="Club Reference ID"
    )

    club = relationship("Club", back_populates="players")
