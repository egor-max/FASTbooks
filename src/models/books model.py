from sqlalchemy import (
    Column,
    Integer,
    String,
)
from core.db import Base


class Book(Base):
    """
    Модель для хранения книг в базе данныйх

    Attributes
    ----------
    Base : _type_
        _description_
    """

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, index=True)
    author = Column(String)
    description = Column(String)
