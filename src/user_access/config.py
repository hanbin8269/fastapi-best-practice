from dataclasses import dataclass
from os import environ


@dataclass
class Config:
    TRUSTED_HOSTS = ["*"]
    DEBUG: bool = False

    MONGO_HOST= environ.get("MONGO_HOST", "mongo")
    MONGO_PORT = int(environ.get("MONGO_PORT", 27017))
    MONGO_INITDB_ROOT_USERNAME = environ.get("MONGO_INITDB_ROOT_USERNAME", "root")
    MONGO_INITDB_ROOT_PASSWORD = environ.get("MONGO_INITDB_ROOT_PASSWORD", "password")

    JWT_SECRET_KEY: str = environ.get("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = environ.get("JWT_ALGORITHM", "HS256")

    GITHUB_API_TOKEN: str = environ.get("GITHUB_API_TOKEN", None)
    GITHUB_API_CLIENT_ID: str = environ.get("GITHUB_API_CLIENT_ID", None)
    GITHUB_API_CLIENT_SECRET: str = environ.get("GITHUB_API_CLIENT_SECRET", None)
    GITHUB_OAUTH_REDIRECT_URI: str = environ.get("GITHUB_OAUTH_REDIRECT_URI", None)


@dataclass
class DevelopConfig(Config):
    TRUSTED_HOSTS = ["*"]
    DEBUG: bool = True

    JWT_SECRET_KEY: str = environ.get("JWT_SECRET_KEY","thisissecretkey")


@dataclass
class ProductConfig(Config):
    TRUSTED_HOSTS = ["*"]
    DEBUG: bool = False

    JWT_SECRET_KEY: str = environ.get("JWT_SECRET_KEY")

def load_config() -> Config:
    config = dict(product=ProductConfig, develop=DevelopConfig)
    return config[environ.get("API_ENV", "develop")]()


CONFIG = load_config()