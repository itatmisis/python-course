from fastapi import FastAPI

app = FastAPI()
counter = 0


@app.get("/")
async def root() -> dict[str, str | int]:
    global counter
    counter += 1
    return {"message": "Hello World", "counter": counter}
