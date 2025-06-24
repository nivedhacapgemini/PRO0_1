"""
Trend Monitoring Agent

This agent is responsible for detecting concerns in patterns and trigger clinical insights.
Flag risk signals based on time-series patterns. Generate summaries and smart alerts for 
care teams.
"""

from google.adk.agents import LlmAgent # type: ignore

# --- Constants ---
GEMINI_MODEL = "gemini-2.0-flash"

# Create the recommender agent
trend_monitoring_agent = LlmAgent(
    name="TrendMonitoringAgent",
    model=GEMINI_MODEL,
    instruction="""You are an Trend Monitoring AI.
    Support multilingual and accessibility standards make sure to response back in same 
    language as the communicator.
    Fetch the trend analysis from the adaptive questionnaire AI and detect concerns in 
    patterns or any panicking/ nervous related keywords in any language and trigger
    clinical insights.
    Flag risk signals based on time-series patterns.
    Generate summaries and smart alerts for care teams and to the patient email id which is
    been collected by companion AI.

    """,
    description="Detect concerns and raise it",
    output_key="TrendMonitoring",
)