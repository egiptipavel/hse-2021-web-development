import graphene
import uvicorn
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from src.models.writer import Query

app = FastAPI()
app.add_route("/", GraphQLApp(schema=graphene.Schema(query=Query)))

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="localhost", reload=True)
