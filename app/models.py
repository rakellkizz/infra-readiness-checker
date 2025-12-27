"""
Data models for infrastructure readiness evaluation.

This module defines:
- Input structure describing a system
- Output structure representing the evaluation result
"""

from enum import Enum
from typing import Dict, List
from pydantic import BaseModel


class CheckStatus(str, Enum):
    """
    Possible status for each infrastructure check.
    """
    OK = "OK"
    PARTIAL = "PARTIAL"
    MISSING = "MISSING"


class SystemInput(BaseModel):
    """
    Describes the infrastructure characteristics of a system
    to be evaluated.
    """

    has_healthcheck: bool
    uses_docker: bool
    has_ci: bool
    uses_orchestration: bool
    has_logging: bool
    is_stateless: bool
    has_tls: bool
    uses_secrets_management: bool


class EvaluationResult(BaseModel):
    """
    Final evaluation output.
    """

    score: int
    status: str
    checks: Dict[str, CheckStatus]
    recommendations: List[str]
