from pydantic_settings import BaseSettings


class DbSettings(BaseSettings):
    pass


class AppSettings(BaseSettings):
    pass


class settings(BaseSettings, DbSettings, AppSettings):
    pass
