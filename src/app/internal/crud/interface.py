from abc import ( 
    ABC,
    abstractmethod,
)


class AbstractCRUD(ABC):
    """
    
    
    """
    @abstractmethod
    async def create(self, obj, session):
        """_summary_

        Args:
            object (_type_): _description_
            session (_type_): _description_
        """
        pass

    
    @abstractmethod
    async def read(self, title, session):
        """_summary_

        Args:
            title (_type_): _description_
            sesion (_type_): _description_
        """
        pass


    @abstractmethod
    async def read_all(self,session):
        """_summary_

        Args:
            session (_type_): _description_
        """
        pass


    @abstractmethod
    async def update(self, obj, new_obj, session):
        """_summary_

        Args:
            object (_type_): _description_
            session (_type_): _description_
        """
        pass


    @abstractmethod
    async def delete(self, title, session):
        """_summary_

        Args:
            title (_type_): _description_
            session (_type_): _description_
        """
        pass
