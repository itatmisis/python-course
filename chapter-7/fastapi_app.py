from fastapi import FastAPI

app = FastAPI()
counter = 0


@app.get("/")
async def root():
    global counter
    counter += 1
    return {"message": "Hello World", "counter": counter}
