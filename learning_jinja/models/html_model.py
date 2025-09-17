import re

from pydantic import BaseModel, Field, model_serializer, model_validator


class HTMLCustom(BaseModel):
    title: str = Field(max_length=100)
    user_name: str = Field(max_length=10)
    user_role: str = Field(max_length=10)
    is_active: bool

    @model_validator(mode="after")
    def validate_after(cls, value: "HTML"):
        if not re.match(f"[A-Za-z0-9]+$", value.user_name):
            raise ValueError("user_name must be alphanumeric")

        if not re.match(r"^[A-Za-z0-9]+$", value.user_role):
            raise ValueError("user_role must be alphanumeric")

        return value

    @model_serializer
    def serialize(self):
        return {
            "title": self.title,
            "name": self.user_name,
            "role": self.user_role,
        }
