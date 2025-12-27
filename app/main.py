"""
API entrypoint for infrastructure readiness evaluation.

This module exposes a minimal HTTP interface that receives
system characteristics and returns an infrastructure readiness
assessment.
"""

from fastapi import FastAPI
from app.models import SystemInput, EvaluationResult
from app.rules import evaluate_system


# ------------------------------------------------------------------------------
# Application instance
# ------------------------------------------------------------------------------

app = FastAPI(
    title="Infrastructure Readiness Checker",
    description="Evaluates if a system meets minimum infrastructure requirements",
    version="1.0.0"
)


# ------------------------------------------------------------------------------
# Endpoints
# ------------------------------------------------------------------------------

@app.post("/evaluate", response_model=EvaluationResult)
def evaluate(system: SystemInput) -> EvaluationResult:
    """
    Evaluate infrastructure readiness for a given system.

    Input:
        - SystemInput: describes infrastructure characteristics

    Output:
        - EvaluationResult: score, status, checks and recommendations
    """

    # Delegate all evaluation logic to the rules engine
    result = evaluate_system(system)

    return result


@app.get("/health")
def health() -> dict:
    """
    Healthcheck endpoint.

    Used by:
    - load balancers
    - orchestrators
    - monitoring systems
    """

    return {"status": "healthy"}
