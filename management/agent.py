"""
Management Agent

This defines the root agent for the PRO0_1 system using the Agent Development Kit (ADK).
The Management Agent is a high-level coordinator responsible for delegating tasks to 
specialized sub-agents based on the nature of the request. It initializes once at startup 
and maintains minimal internal state.
"""

from google.adk.agents import Agent # type: ignore

# Import the subagents
from .sub_agents.companion_agent.agent import companion_agent
from .sub_agents.adaptive_questionnaire_agent.agent import adaptive_questionnaire_agent
from .sub_agents.trend_monitoring_agent.agent import trend_monitoring_agent

root_agent = Agent(
    name="management",
    model="gemini-2.0-flash",
    description="Oversees and delegates tasks to sub-agents, ensuring efficient task" \
                " distribution and multilingual communication",
    instruction="""
    You are a Management agent that is responsible for overseeing the work
    of the other agents also can communicate in any languages and response back in same language as the communicator.
    Ensure transparency, consent, and data privacy compliance.
    Track success through completion rate, alert accuracy, and user satisfaction.

    Always delegate the task to the appropriate agent. Use your best judgement 
    to determine which agent to delegate to.

    You are responsible for delegating tasks to the following agent:
    - companion_agent for checkin activities
    - adaptive_questionnaire_agent for any health issues raised
    - trend_monitoring_agent to analysis the risk in a frequent time interval
    Support multilingual communication if needed.
    """,
    sub_agents=[companion_agent, adaptive_questionnaire_agent, trend_monitoring_agent],
)