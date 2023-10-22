import uvicorn
from fastapi import FastAPI

import users

app = FastAPI(title="Python Course", description="Base Template for learning FastAPI")
app.include_router(users.router)


@app.get("/")  # method + path
async def say_hello():  # async/sync + name in docs
    return {"message": "Hello World"}  # response


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    # http://localhost:8000/docs
