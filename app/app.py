from typing import List

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

player_router = APIRouter(
    prefix="/player",
    tags=["player"],
    dependencies=[],
    responses={404: {"description": "Not found"}}
)

from starlette import status


# from . import crud, models
# from schema import club, player, stadium
# from .database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)

DESC = """
🏆 LaLiga API ⚽️ (_Season 21-22_)

You will be able to:

# Player

* **Create players** (_not implemented_).
* **Read players** (_not implemented_).

# Club

* **Read clubs** (_not implemented_).
"""

# Tags is constrained by order!!!
API_TAGS = [
    {
        "name": "player",
        "description": "About players",
        # "externalDocs": {
        #     "description": "Move LaLiga Players",
        #     "url": "https://www.laliga.com/en-GB"
        # }
    },
    {
        "name": "club",
        "description": "About clubs"
    },
]

app = FastAPI(
    title="LaLiga-API",
    # description="About LaLiga Information Season 21-22",
    description=DESC,
    version="0.1",
    # terms_of_service="https://fastapi.tiangolo.com",
    contact={
        "name": "Devamos",
        "url": "https://github.com/minho-lee0716",
        "email": "minho.lee0716@gmail.com"
    },
    license_info={
        "name":"Min-Ho Lee",
        "url":"https://github.com/minho-lee0716"
    },
    # openapi_tags=API_TAGS,
    openapi_url="/docs.json",
    # openapi_url=None,
    docs_url="/docs",
    # redoc_url=None
)


@app.get("/player", tags=["player"], summary="All players who play in LaLiga")
async def player():
    """
        **id** : Primary key\n
        name: Player name\n
        club: Affiliated club team name
    """
    return [
        {"id": 1, "name": "Karim Benzema", "club": "RealMadrid"},
        {"id": 2, "name": "Vinicius Jr", "club": "RealMadrid"},
    ]


@app.get("/club", tags=["club"], summary="All clubs in LaLiga")
async def club():
    return {}


# @app.get("/player/")


# Dependency

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/player")
# def create_player(player: player.PlayerCreate, db: Session = Depends(get_db())):
#     db_player = crud.create_player(db, player=player)
#     print(db_player)
#     return {}

# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
#
#
# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
#
#
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)
#
#
# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age
