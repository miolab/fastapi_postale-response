from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RequestBodyDummy(BaseModel):
    status: str


class UserDummy(BaseModel):
    name: str
    lang: str


@app.post('/')
def post_status_dummy(req: RequestBodyDummy):
    """POST handler: for req and res test in root"""
    match status := req.status:
        case "ping":
            return {"status": "pong"}
        case "ok":
            return {"status": status}
        case _:
            return {"status": "error"}


@app.post('/user_dummy/')
def post_user_dummy(user: UserDummy):
    """POST handler: for req and res test"""
    return {
        "name": user.name,
        "lang": user.lang
    }


@app.get('/hello/{user_id}')
def get_hello_world(user_id: int, q: str = ""):
    """Get handler: for test"""
    return {
        "user_id": user_id,
        "query": q,
        "message": "Hello, world!"
    }


@app.get('/')
def get_root():
    """Get handler: root endpoint"""
    return {
        "message": "Hello, this is GET root."
    }
