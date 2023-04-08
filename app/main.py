from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    user_id: int

@app.get('/hello/{user_id}')
async def get_hello_world_test(user_id: int):
    """Get handler: for test"""
    return {
        "user_id": user_id,
        "message": "Hello, world!"
    }
