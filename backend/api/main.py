"""
main.py — FastAPI application for Synthetic Nation.

Runs at http://localhost:8000
CORS enabled for frontend at http://localhost:5173 (Vite dev server).
"""

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes import simulation, causal, policy, validation

app = FastAPI(
    title="Synthetic Nation API",
    description="Policy simulation engine with autonomous multi-tier agents",
    version="1.0.0",
)

# CORS for Vite dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(simulation.router, prefix="/api")
app.include_router(causal.router, prefix="/api")
app.include_router(policy.router, prefix="/api")
app.include_router(validation.router, prefix="/api")


@app.get("/api/health")
async def health():
    return {"status": "ok", "service": "synthetic-nation"}
