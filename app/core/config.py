from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "Restful API"

    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_USER: str
    EMAIL_PASS: str

    SITE_A_EMAIL: str
    SITE_B_EMAIL: str
    SITE_C_EMAIL: str

    class Config:
        env_file = ".env"


settings = Settings()
