from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from core.db import Base


class Book(Base):
    """
    Модель для хранения книг в базе данных.

    Attributes
    ----------
    id: int
        Первичный ключ в базе данных.
    title: str
        Название книги.
    author: str
        Автор книги.
    description: str
        Краткое описание книги.
            
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    description: Mapped[str]
