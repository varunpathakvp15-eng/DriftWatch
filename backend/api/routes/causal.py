"""
causal.py — /api/causal/{simulation_id}/{metric}/{day} endpoint.

Returns causal chain tree for why a metric has its value at a given day.
"""

from __future__ import annotations

from fastapi import APIRouter

from backend.api.demo_data import CAUSAL_CHAIN_DAY18

router = APIRouter()


@router.get("/causal/{simulation_id}/{metric}/{day}")
async def get_causal_chain(simulation_id: str, metric: str, day: int):
    """Get causal chain tree for a metric at a specific day.

    Returns a tree of agent clusters and their decisions that
    causally contribute to the metric's value.
    """
    # For demo, return the pre-computed causal chain for day 18 protest
    if metric == "protest_probability" and day >= 15:
        return {
            "simulation_id": simulation_id,
            "metric": metric,
            "day": day,
            "chain": CAUSAL_CHAIN_DAY18,
        }

    # Generic causal chain for other metrics
    return {
        "simulation_id": simulation_id,
        "metric": metric,
        "day": day,
        "chain": {
            "metric": metric,
            "value": 0.0,
            "day": day,
            "root": {
                "label": f"Causal analysis for {metric} at day {day}",
                "agent_count": 0,
                "children": [
                    {
                        "label": "Policy impact propagation",
                        "agent_count": 5000,
                        "decision": "Direct fare impact on commuting costs",
                        "children": [],
                    },
                    {
                        "label": "Network cascade effects",
                        "agent_count": 2000,
                        "decision": "Tier 2 broadcast amplification",
                        "children": [],
                    },
                ],
            },
        },
    }
