from fastapi import FastAPI
from dotenv import load_dotenv
from src.api.v1.router import api_router

load_dotenv()

app = FastAPI(
    title="Apply Buddy API",
    description="Backend API for Apply Buddy Chrome Extension",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}