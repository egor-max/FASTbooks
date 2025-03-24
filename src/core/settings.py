from pydantic_settings import (
    BaseSettings, 
    SettingsConfigDict,
)


class PostgresSqlSettings(BaseSettings):
    """
    Настройки для подключения к базе данных.
    
    Параметры задаются через переменные окружения, указанные в .env.

    Attributes 
    ----------
    DATABASE_URL : str
        URL подключение к базе данных.
    
    """

    database_url: str
    model_config = SettingsConfigDict(      #  Изучить SettingsConfigDict
                                            #  Установить зависимость 
        env_file=".env", 
        env_file_encoding="utf-8",
        
    )
    

class AppSettings(BaseSettings):
    """
    Настройки параметров FastAPI приложения.

    Параметры задаются через переменные окружения, указанные в .env.

    Attributes 
    ----------

    """


class Settings(BaseSettings, PostgresSqlSettings, AppSettings): 
    """
    Настройки проекта для запуска приложения.

    Параметры задаются через родительские классы.

    Attributes 
    ----------
    None

    """
