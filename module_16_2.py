from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def welcome() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{username}/{age}")
async def user_inf(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


@app.get("/user/{user_id}")
async def user_id(user_id: Annotated[int, Path(ge=1, le=100, description='Enter user ID', example=5)]) -> str:
    return f"Вы вошли как пользователь № {user_id}"
