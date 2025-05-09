# small application that validates and processes data from a JSON file containing inventory items for a store (not a user-based example, as requested).
# The exercise focuses on using Pydantic’s core features, including field constraints, custom validators, and serialization, and avoids theoretical explanations to keep it hands-on.
# You’ll create a Pydantic model, add validation logic, and process a JSON file, with a clear goal and steps to follow.
import json

# Requirements
# Fields:
# item_id: String, must be a non-empty alphanumeric ID (e.g., “A123”).
# name: String, non-empty, max length 50 characters.
# price: Float, must be positive.
# quantity: Integer, must be non-negative.
# category: String, must be one of “Electronics”, “Clothing”, “Books”, or “Food”.


# Validation Rules:
# item_id must match the pattern ^[A-Za-z0-9]+$ (alphanumeric only).
# price must not exceed 1000.0.
# If quantity is 0, add a warning but allow the item.
# Ensure name is title-cased (e.g., “laptop” → “Laptop”).


# Tasks:
# Load and validate the JSON file.
# Calculate the total inventory value (sum of price × quantity for all valid items).
# Filter and list items in the “Electronics” category.
# Output warnings for zero-quantity items and errors for invalid items.


# below are the steps
# 1. create pydantic model
# 2. process the json file
# 3. main function

from pydantic import (
    BaseModel,
    Field,
    validator,
    field_validator,
    field_serializer,
    model_validator,
    model_serializer,
    SecretStr,
    ValidationError,
)
import re
from pathlib import Path


class Item(BaseModel):
    item_id: str
    name: str = Field(max_length=20)
    price: float = Field(gt=0.0)
    quantity: int = Field(ge=0)
    category: str = Field(default=None)

    @field_validator("name")
    def validate_name(cls, value):
        if not re.match(f"[A-Za-z0-9]+$", value):
            raise ValueError("item_id must be alphanumeric")

        return value

    @field_validator("price")
    def validate_price(cls, value):
        print("inside quantity")
        if value == 0:
            raise ValueError("price must be greater than 0")
        return value

    @field_validator("quantity")
    def validate_quantity(cls, value):

        if value == 0:
            print("th3e value cant be zero")
        return value

    @model_validator(mode="after")
    def validate_mode(cls, value: "Item"):
        if value.category == "Electronics" and value.price < 1000:
            raise ValueError("price must be greater than 1000 for Electronics")
        return value


def process_inventory_frm_json(json_file_path: Path) -> tuple[float, list[Item]]:
    valid_items: list[Item] = list()
    total_price: float = 0.0
    with open(json_file_path) as json_file:
        data = json.load(json_file)

    for item in data:
        try:
            validated_item = Item(
                item_id=item["item_id"],
                name=item["name"],
                price=item["price"],
                quantity=item["quantity"],
                category=item["category"],
            )
            # Item.model_validate(validated_item,strict=True)
            valid_items.append(item)
            total_price += validated_item.price * validated_item.quantity

        except ValidationError as e:
            print(e)

    return total_price, valid_items


def main():
    json_file_path: Path = Path(__file__).parent.joinpath("data", "inventory.json")
    total_price, valid_items = process_inventory_frm_json(json_file_path)
    print(total_price)
    for item in valid_items:
        print(item)


if __name__ == "__main__":
    main()
