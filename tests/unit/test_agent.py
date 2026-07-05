"""Performance Review Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_draft_review():
    """Test Draft a performance review based on goals, feedback, and achievements."""
    tools = AgentTools()
    result = await tools.draft_review(employee_id="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_aggregate_feedback():
    """Test Aggregate and synthesize 360-degree feedback for an employee."""
    tools = AgentTools()
    result = await tools.aggregate_feedback(employee_id="test", feedback_sources="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_analyze_calibration():
    """Test Analyze rating distribution for calibration issues across a team."""
    tools = AgentTools()
    result = await tools.analyze_calibration(manager_id="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_goals():
    """Test Track progress on employee goals and OKRs."""
    tools = AgentTools()
    result = await tools.track_goals(employee_id="test", period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.performance_review_agent_agent import PerformanceReviewAgentAgent
    agent = PerformanceReviewAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
