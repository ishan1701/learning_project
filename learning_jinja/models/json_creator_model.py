from enum import Enum

from pydantic import (BaseModel, Field, HttpUrl, field_validator,
                      model_serializer, model_validator)


class AppEnvironment(Enum):
    development = "development"
    production = "production"
    qa = "qa"


class DatabaseConfig(BaseModel):
    """
    Database config model. It is based on the inouts.yaml
    """

    host: str = Field(max_length=50)
    port: int = Field(ge=1, le=65535)
    name: str = Field(max_length=50)
    username: str = Field(max_length=50)


class APIModel(BaseModel):
    """
    Model for APIs
    """

    name: str = Field(max_length=50)
    url: HttpUrl
    enabled: bool


class APIConfig(BaseModel):
    app_name: str = Field(max_length=50)
    environment: AppEnvironment = Field(default=AppEnvironment.development)
    database: DatabaseConfig
    api_endpoints: list[APIModel]
