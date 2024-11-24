from fastapi import FastAPI

app = FastAPI()


@app.get('/user/admin')
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get('/user/{user_id}')
async def polzovatel(user_id: str) -> dict:
    return {"message": f"Вы вошли как пользователь {user_id}"}


@app.get('/user')
async def ctranizi(username: str, age: str) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}


@app.get('/')
async def welcome() -> dict:
    return {"message": "Главная страница"}