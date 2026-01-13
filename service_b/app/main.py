from fastapi import FastAPI
import uvicorn
from . import routes

app = FastAPI()


app.include_router(
    routes.router
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)