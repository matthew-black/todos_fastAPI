from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

# SQLAlchemy creates the "todos" table:
  # (Note: You'll need to use alembic for migrations)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Yields a database connection:
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

@app.get("/todos", response_model=list[schemas.Todo])
def read_todos(db: Session = Depends(get_db)):
    todos = crud.get_todos(db,)
    return todos

@app.get("/todos/{todo_id}", response_model=schemas.Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo(db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@app.post("/todos", response_model=schemas.Todo, status_code=201)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    new_todo = crud.create_todo(db=db, todo=todo)
    return new_todo
