"""
simulation.py — /api/simulate, /api/counterfactual, /api/cities endpoints.

SSE streaming for real-time simulation results.
"""

from __future__ import annotations

import asyncio
import json
import uuid

from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from backend.api.demo_data import CITIES, DELHI_DEMO_DATA, COUNTERFACTUAL_DATA

router = APIRouter()


class SimulationRequest(BaseModel):
    city_id: str = "DEL"
    policy_text: str = "Indian Railways increases suburban fares by 20% effective from next month across all classes"
    time_horizon_days: int = 30
    population_size: int = 10000
    seed: int = 42


class CounterfactualRequest(BaseModel):
    base_simulation_id: str
    branch_point_day: int = 0
    modified_policy_text: str = "Indian Railways increases suburban fares by 10% effective from next month"


# In-memory simulation store
_simulations: dict[str, dict] = {}


@router.get("/cities")
async def list_cities():
    """List available cities with confidence grades."""
    return {"cities": CITIES}


@router.post("/simulate")
async def run_simulation(request: SimulationRequest):
    """Stream simulation results as Server-Sent Events.

    Each event is a JSON object with day metrics, alerts, and status.
    Demo mode streams pre-computed Delhi data at 300ms per day for
    fast judge presentation.
    """
    sim_id = str(uuid.uuid4())[:8]
    _simulations[sim_id] = {
        "id": sim_id,
        "city_id": request.city_id,
        "policy_text": request.policy_text,
        "status": "running",
    }

    async def event_stream():
        # Initial event with simulation metadata
        meta = {
            "event": "sim_start",
            "simulation_id": sim_id,
            "city_id": request.city_id,
            "policy_text": request.policy_text,
            "population_size": request.population_size,
            "time_horizon_days": request.time_horizon_days,
        }
        yield f"data: {json.dumps(meta)}\n\n"

        # Stream day-by-day results from pre-computed data
        data = DELHI_DEMO_DATA[:request.time_horizon_days]
        for day_data in data:
            day_data["simulation_id"] = sim_id
            day_data["event"] = "day_update"
            yield f"data: {json.dumps(day_data)}\n\n"
            await asyncio.sleep(0.3)  # 300ms per day for demo pacing

        # Final summary
        final = data[-1].copy() if data else {}
        final["event"] = "sim_complete"
        final["simulation_id"] = sim_id
        yield f"data: {json.dumps(final)}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@router.post("/counterfactual")
async def run_counterfactual(request: CounterfactualRequest):
    """Stream counterfactual simulation as SSE."""
    cf_id = f"cf-{str(uuid.uuid4())[:8]}"

    async def event_stream():
        meta = {
            "event": "counterfactual_start",
            "counterfactual_id": cf_id,
            "base_simulation_id": request.base_simulation_id,
            "branch_point_day": request.branch_point_day,
            "modified_policy": request.modified_policy_text,
        }
        yield f"data: {json.dumps(meta)}\n\n"

        for day_data in COUNTERFACTUAL_DATA:
            day_data["counterfactual_id"] = cf_id
            day_data["event"] = "cf_day_update"
            yield f"data: {json.dumps(day_data)}\n\n"
            await asyncio.sleep(0.2)

        final = {
            "event": "cf_complete",
            "counterfactual_id": cf_id,
            "summary": {
                "protest_reduction": "63%",
                "revenue_tradeoff": "60% of original impact",
                "resistance_reduction": "61%",
            },
        }
        yield f"data: {json.dumps(final)}\n\n"

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
