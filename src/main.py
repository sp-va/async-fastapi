import uvicorn
from fastapi import FastAPI

from routers.documents import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host= "172.18.0.2", port=8008, reload=True)