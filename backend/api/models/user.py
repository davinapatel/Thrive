from sqlalchemy import Column, String, Integer, VARCHAR
from database import Base

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(VARCHAR(8), nullable=False)

    def __repr__(self):
        return '<Username %r>' % self.username