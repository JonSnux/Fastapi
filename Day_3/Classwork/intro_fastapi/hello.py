import asyncio

from fastapi import Body, FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return 'Hello, World!'


@app.get('/hello/{who}')
def hello_named(who:str):
    return f'Hello, {who}!'


@app.get('/hello')
def hello_query(who: str):
    return f'Hi, {who}!'


@app.post('/hello')
def body_name(who = Body(embed=True)):
    return f'Hello, {who}!'
    

class User(BaseModel):
    name: str
    age: int | None = None


@app.post('/user')
def create_user(user: User) -> str:
    print(f'Out: {type(user)}')
    return f'Hello, {user.name}. You are {user.age or 0}'


@app.get('/async_hello')
async def get_async_url():
    await asyncio.sleep(1)
    return f"Done."

if __name__ == '__main__':
    uvicorn.run('hello:app', reload=True)