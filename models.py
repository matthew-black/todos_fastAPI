from sqlalchemy import Boolean, Column, Integer, String

from database import Base


# The SQLAlchemy model for a todo:
class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True)
    todo_text = Column(String, unique=True, index=True)
    is_complete = Column(Boolean, default=False, server_default='false')
