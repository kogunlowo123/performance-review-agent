"""Test configuration for Performance Review Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "performance-review-agent", "category": "Human Resources"}
