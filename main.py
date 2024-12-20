from fastapi import FastAPI

app = FastAPI()


# Определение базового маршрута
@app.get("/")
async def welcome() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user")
async def user_inf(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


@app.get("/user/{user_id}")
async def user_id(user_id: str) -> str:
    return f"Вы вошли как пользователь № {user_id}"
