from fastapi import FastAPI
from app.routes import test

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the app backend service!"}

# Include routes
app.include_router(test.router)