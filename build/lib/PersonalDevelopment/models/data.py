from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey)

from .meta import Base


class Data(Base):
    """ Таблица данных пользователей """
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    user_login = Column(ForeignKey('users.login'))
    data = Column(Text, nullable=False)

    def __repr__(self):
        return 'id={} user_id={} data={}'.format(self.id, self.user_login, self.data)
