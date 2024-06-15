from pydantic import BaseModel


# The Pydantic schema for a todo:
class TodoBase(BaseModel):
    todo_text: str

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    id: int
    is_complete: bool

    class Config:
        orm_mode = True
