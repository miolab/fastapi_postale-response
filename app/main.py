from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/hello/{user_id}')
async def get_hello_world_test(user_id: int, q: str = ""):
    """Get handler: for test"""
    return {
        "user_id": user_id,
        "query": q,
        "message": "Hello, world!"
    }
