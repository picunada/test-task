import uvicorn
from fastapi import FastAPI

from router import equations, colors
from db.connect import database

app = FastAPI(title="test-task")

app.include_router(equations.router, prefix="/equation", tags=["Get solution for equation"])
app.include_router(colors.router, prefix="/colors", tags=["Guess the color"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database  .disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)
