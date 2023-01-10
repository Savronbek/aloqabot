from base import BaseModel
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey



class User(BaseModel):
    __tablename__ = 'users'

    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)

    username = Column(VARCHAR(32), unique=False, nullable=True)

    reg_date = Column(DATE, default=datetime.date.today())

    upd_date = Column(DATE, onupdate=datetime.date.today())

    def __str__(self) -> str:
        return f"<User:{self.user_id}>"
    



class Player(BaseModel):
    """ Таблица игроков """
    __tablename__ = 'Players'

    tg_id = Column(Integer, unique=True, primary_key=True, nullable=True)
    name = Column(String(80), nullable=True)
    score = Column(Integer)

    def __repr__(self):
        return "<User(tg_id='%s', name='%s', current_q_id='%s, is_finished='%s')>" % (self.tg_id, self.name, self.current_q_id, self.is_finished)
