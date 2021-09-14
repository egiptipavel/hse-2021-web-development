import uvicorn
from fastapi import FastAPI

from endpoints import animals

app = FastAPI()
app.include_router(animals.router)


@app.get('/')
def home():
    return "Hello World!"


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="localhost", reload=True)
