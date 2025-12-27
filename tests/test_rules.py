"""
Tests for infrastructure readiness rules.
"""

from app.models import SystemInput
from app.rules import evaluate_system


def test_system_ready():
    """
    Fully compliant system should be READY with high score.
    """
    system = SystemInput(
        has_healthcheck=True,
        uses_docker=True,
        has_ci=True,
        uses_orchestration=True,
        has_logging=True,
        is_stateless=True,
        has_tls=True,
        uses_secrets_management=True,
    )

    result = evaluate_system(system)

    assert result.status == "READY"
    assert result.score >= 80
    assert "healthcheck" in result.checks


def test_system_not_ready():
    """
    System missing critical infrastructure elements
    should be marked as NOT READY.
    """
    system = SystemInput(
        has_healthcheck=False,
        uses_docker=False,
        has_ci=False,
        uses_orchestration=False,
        has_logging=False,
        is_stateless=False,
        has_tls=False,
        uses_secrets_management=False,
    )

    result = evaluate_system(system)

    assert result.status == "NOT READY"
    assert result.score < 50
    assert len(result.recommendations) > 0
