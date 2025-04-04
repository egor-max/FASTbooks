from sqlalchemy import (
    Column,
    Integer,
    String,
    Mapped,
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

    id: Mapped[Integer]
    title: Mapped[String]
    author: Mapped[String]
    description:Mapped[String]
