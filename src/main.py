from fastapi import FastAPI
from src.routers import user

app = FastAPI(title="CI/CD Lab App")

app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "CI/CD Lab is running"}