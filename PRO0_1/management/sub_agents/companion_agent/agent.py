"""
Companion Agent

This agent is responsible for Initiate conversational check-ins with patients managing 
chronic conditions. Adapt tone, complexity, and delivery mode based on behavior and 
comprehension signals.
"""

from google.adk.agents import Agent # type: ignore
from google.adk.tools.tool_context import ToolContext # type: ignore

def handle_checkin(user_input: str, tool_context: ToolContext) -> dict:
    # When check-in starts
    tool_context.state["checkin_started"] = True
    print("Check-in started")

    if "stress" in user_input or "sleep" in user_input:
        # When user provides a meaningful health-related response
        tool_context.state["checkin_completed"] = True
        print("Check-in completed")
        
        return {
            "status": "success",
            "response": "Thanks for sharing. Let's explore this further...",
        }

    return {
        "status": "in_progress",
        "response": "Can you tell me more about how you're feeling?",
    }


# companion agent
companion_agent = Agent(
    name="companion_agent",
    model="gemini-2.0-flash",
    description="Check-ins management",
    instruction="""You are an Companion AI.

    Initiate conversational check-ins with patients managing chronic conditions
    Adapt to the tone, complexity, and delivery mode based on behavior and comprehension 
    signals.

    - Adjust your tone and complexity to match their emotional state and comprehension.
    - Support multilingual communication if needed.

    Ensure the conversation is empathetic, respectful, and patient-centered.
    
    If the user asks about anything else, you should delegate the task to the manager agent.
    """,
    output_key="checkins",
)