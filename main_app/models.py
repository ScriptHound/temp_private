from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(255), nullable=False, unique=True)
    path = Column(String(255), nullable=False, unique=True)

    def __repr__(self):
        return "<Image(id='%s', path='%s', uuid='%s)>" % (
            self.id, self.path, self.uuid)

