"""
Adaptive Questionnaire Agent to personalize delivery

This agent is responsible for Detecting emotional cues and adjust question flow or offer 
reassurance in response.
Support multilingual and accessibility standards. Collect and organize PRO data over time 
for trend analysis.
"""

from google.adk.agents import LlmAgent # type: ignore

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

from google.adk.tools.tool_context import ToolContext # type: ignore


def adaptive_questionnaire(topic: str, tool_context: ToolContext) -> dict:
    """Get a companion for check ins."""
    print(f"--- Tool: adaptive questionnaire agent called for: {topic} ---")

    responses = {
        "default": "Hello, Welcome!",
        "checkin": "I'll coordinate your check-in!"
    }

    response = responses.get(topic.lower(), responses["default"])

    # Update state
    tool_context.state["history"] = topic

    return {"status": "success", "response": response, "topic": topic}


# Create the recommender agent
adaptive_questionnaire_agent = LlmAgent(
    name="AdaptiveQuestionnaireAgent",
    model=GEMINI_MODEL,
    instruction="""You are an Adaptive Questionnaire AI.

    Offer reassurance if distress or confusion is detected.
    Encourage them to share symptoms, concerns, or changes in their condition.
    If the user says explicitly panicking over the situation, you should ask the trend
    monitoring agent to trigger alerts to the care teams.
    Detecting emotional cues and adjust question flow or offer reassurance in response.
    Support multilingual and accessibility standards make sure to response back in same
    language as the communicator.
    Collect and organize PRO data over time for trend analysis for the trend_monitoring_agent.

    """,
    description="personalize delivery",
    output_key="personDev",
)