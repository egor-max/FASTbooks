from src.app.internal.crud.interface import AbstractCRUD
from src.app.internal.schemas import BooksCreateSchema
from src.app.internal.models import Book


class CRUDOperations(AbstractCRUD):

    async def create(self, obj, session):

        result = BooksCreateSchema(**obj)

        session.add(result)
        session.commit()
        session.refresh()

        return result
    

    async def read(self, title, session):
        return session.get(Book, title)
    
    
    async def read_all(self, session):
        return session.get(Book)
    

    async def update(self, obj, new_obj, session):
        
        stm = session.get(Book, obj)

        if not stm:
            return None
        
        for k, v in new_obj.items():
            if hasattr(obj, k):
                setattr(obj, k, v)
        
        session.add(obj)
        session.commit()
        session.refresh()

        return obj
    

    async def delete(self, title, session):

        stm = session.get(Book, title)

        if not stm:
            return None
        
        session.delete(stm)
        session.commit()
        session.refresh()

        return stm
    

crud_operation = CRUDOperations()
