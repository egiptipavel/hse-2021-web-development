import uvicorn
from fastapi import FastAPI

from src.endpoints.components import router as components
from src.endpoints.orders import router as orders
from src.endpoints.users import router as users
from src.sql_app import models
from src.sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(components)
app.include_router(orders)
app.include_router(users)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
