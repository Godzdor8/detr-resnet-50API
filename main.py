import uvicorn
from fastapi import FastAPI
from API import *

app = FastAPI()
app.include_router(apps)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
