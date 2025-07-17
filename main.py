from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="MCP Server")

app.include_router(router)
