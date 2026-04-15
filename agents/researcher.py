"""
Research Agent - Gathers and synthesizes information about topics.
"""

from crewai import Agent


def create_researcher_agent():
    """
    Creates a research agent that gathers comprehensive information
    about topics and synthesizes it into a research report.
    
    Note: LLM is configured through environment variables set in config.py
    """
    return Agent(
        role="Research Agent",
        goal="Conduct thorough research on topics and provide comprehensive, well-organized research reports",
        backstory="""You are an experienced research analyst with expertise in finding, evaluating, 
        and synthesizing information from multiple sources. You excel at identifying key insights, 
        organizing complex information, and presenting findings in a clear, structured manner. 
        Your research is always accurate, well-sourced, and comprehensive.""",
        verbose=True,
        allow_delegation=False,
    )
