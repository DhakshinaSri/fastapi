from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog import schemas, database
from blog.repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
    )

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)) -> schemas.ShowUser:
    return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUser, status_code=status.HTTP_200_OK)
def show_user(id: int, db: Session = Depends(get_db)):
    return user.show_user(id, db)