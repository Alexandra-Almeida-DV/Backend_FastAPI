from fastapi import FastAPI
from app.api.routes import health, contact

app = FastAPI(title="Backend FastAPI")

app.include_router(health.router, prefix="/api")
app.include_router(contact.router, prefix="/api")
