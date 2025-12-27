"""
Evaluation rules for infrastructure readiness.

This module contains pure evaluation logic.
It must NOT depend on the API layer to avoid circular imports.
"""

from typing import Dict, List
from app.models import SystemInput, EvaluationResult, CheckStatus


def evaluate_system(system: SystemInput) -> EvaluationResult:
    """
    Evaluate a system against infrastructure readiness criteria.

    This function contains only business rules and scoring logic.
    It is intentionally framework-agnostic to allow reuse in:
    - API layer
    - CLI tools
    - Batch processing
    - Automated tests
    """

    checks: Dict[str, CheckStatus] = {}
    recommendations: List[str] = []
    score = 0

    # ------------------------------------------------------------------
    # Healthcheck
    # ------------------------------------------------------------------
    if system.has_healthcheck:
        checks["healthcheck"] = CheckStatus.OK
        score += 15
    else:
        checks["healthcheck"] = CheckStatus.MISSING
        recommendations.append("Add a dedicated healthcheck endpoint")

    # ------------------------------------------------------------------
    # Containerization
    # ------------------------------------------------------------------
    if system.uses_docker:
        checks["containerization"] = CheckStatus.OK
        score += 15
    else:
        checks["containerization"] = CheckStatus.MISSING
        recommendations.append("Containerize the application using Docker")

    # ------------------------------------------------------------------
    # Continuous Integration
    # ------------------------------------------------------------------
    if system.has_ci:
        checks["ci"] = CheckStatus.OK
        score += 15
    else:
        checks["ci"] = CheckStatus.MISSING
        recommendations.append("Implement a CI pipeline for automated validation")

    # ------------------------------------------------------------------
    # Orchestration
    # ------------------------------------------------------------------
    if system.uses_orchestration:
        checks["orchestration"] = CheckStatus.OK
        score += 15
    else:
        checks["orchestration"] = CheckStatus.MISSING
        recommendations.append(
            "Prepare the system for orchestration (e.g. Kubernetes)"
        )

    # ------------------------------------------------------------------
    # Logging
    # ------------------------------------------------------------------
    if system.has_logging:
        checks["logging"] = CheckStatus.OK
        score += 10
    else:
        checks["logging"] = CheckStatus.MISSING
        recommendations.append("Implement structured logging")

    # ------------------------------------------------------------------
    # Stateless design
    # ------------------------------------------------------------------
    if system.is_stateless:
        checks["stateless"] = CheckStatus.OK
        score += 10
    else:
        checks["stateless"] = CheckStatus.PARTIAL
        recommendations.append("Remove state dependency from the application")

    # ------------------------------------------------------------------
    # Security basics
    # ------------------------------------------------------------------
    if system.has_tls and system.uses_secrets_management:
        checks["security"] = CheckStatus.OK
        score += 20
    else:
        checks["security"] = CheckStatus.PARTIAL
        if not system.has_tls:
            recommendations.append("Enable TLS for external communication")
        if not system.uses_secrets_management:
            recommendations.append("Move secrets out of source code")

    # ------------------------------------------------------------------
    # Final classification
    # ------------------------------------------------------------------
    if score >= 80:
        status = "READY"
    elif score >= 50:
        status = "PARTIALLY READY"
    else:
        status = "NOT READY"

    return EvaluationResult(
        score=score,
        status=status,
        checks=checks,
        recommendations=recommendations,
    )
