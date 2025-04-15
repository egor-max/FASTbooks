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
    

class AppSettings(BaseSettings):
    """
    Настройки параметров FastAPI приложения.

    Параметры задаются через переменные окружения, указанные в .env.

    Attributes 
    ----------

    """

    app_title: str
    app_description: str
    secret: str


class Settings(AppSettings, BaseSettings, PostgresSqlSettings): 
    """
    Настройки проекта для запуска приложения.

    Параметры задаются через родительские классы.

    Attributes 
    ----------
    None

    """
    
    model_config = SettingsConfigDict(
                
        env_file=".env", 
        env_file_encoding="utf-8",
    )   


settings = Settings()
