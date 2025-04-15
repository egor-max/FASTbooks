from pydantic import(
    BaseModel,
    Field,
)

from src.app.constants import(
    MAX_TITLE_LEN,
    MIN_TITLE_LEN,
)

class BaseBooksSchema(BaseModel):
    """

    
    """
    title: str = Field(..., ge=MIN_TITLE_LEN, lt=MAX_TITLE_LEN)
    author: str
    description: str


class BooksCreateSchema(BaseBooksSchema):
    """
    

    """


class BooksUpdateSchema(BaseBooksSchema):
    """_summary_

    Args:
        BaseBooksSchema (_type_): _description_
    """

class BooksReadSchema(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    title: str


class BooksDeleteSchema(BaseModel):
    """_summary_

    Args:
        BaseBooksSchema (_type_): _description_
    """
    title: str
