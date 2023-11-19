from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/ip", response_class=PlainTextResponse)
def get_client_ip(request: Request) -> str:
    return request.client.host
