from pydantic import BaseModel
from fastapi import Form

class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int | None = None
    item: str

    @classmethod
    def as_form(
            cls,
            item: str = Form(...),
    ):
        return cls(item=item)

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                    "item": "Example schema!"
        }
        }

class TodoItem(BaseModel):
    item: str
    class Config:
        json_schema_extra = {
            "example": {
            "item": "Read the next chapter of the book"
        }
        }