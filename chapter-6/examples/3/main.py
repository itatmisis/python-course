import uvicorn
from fastapi import FastAPI

import users

app = FastAPI(title="Python Course", description="Лучший шаблон, чтобы учить FastAPI")
app.include_router(users.router)


# response_model - возвращаемая модель данных
@app.get("/", response_model=dict[str, str])  # endpoint = method + path
def say_hello() -> dict[str, str]:  # имя функции будет использоваться в документации
    """
    Текст в документаци функции будет использоваться в сваггере
    """
    return {"message": "Hello World"}  # ответ


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    # http://localhost:8000/docs
