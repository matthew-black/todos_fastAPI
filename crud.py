from sqlalchemy.orm import Session

import models, schemas


# CRUD utils for todos:
def get_todo(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def get_todos(db: Session):
    return db.query(models.Todo).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(todo_text=todo.todo_text)
    db.add(db_todo) # add todo instance to session
    db.commit() # inserts todo instance into database table
    db.refresh(db_todo) # refresh the todo instance (AKA: it has an "id" now)
    return db_todo
