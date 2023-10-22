import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Python Course", description="Base Template for learning FastAPI")


@app.get("/")  # method + path
async def say_hello():  # async/sync + name in docs
    return {"message": "Hello World"}  # response


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)  # base url
    # http://localhost:8000/docs

